import sys
input = sys.stdin.readline

def judge(x):
    now, cnt = 0, 0
    
    for i in range(n):
        if now+w[i]<=x:
            now += w[i]
        else:
            cnt += 1
            now = w[i]
    
    if now>0:
        cnt += 1
    
    return cnt<=k

def binary_search():
    l, r = max(w), 10**10
    
    while l<=r:
        m = (l+r)//2
        
        if judge(m):
            r = m-1
        else:
            l = m+1
    
    return l

n, k = map(int, input().split())
w = [int(input()) for _ in range(n)]
print(binary_search())

