import sys
input = sys.stdin.readline

def judge(x):
    B = [A[i] for i in range(N) if i!=x]
    now = A[x]
    
    for Bi in B:
        if Bi>2*now:
            return False
            
        now += Bi
    
    return True

def binary_search():
    l, r = 0, N-1
    
    while l<=r:
        m = (l+r)//2
        
        if judge(m):
            r = m-1
        else:
            l = m+1
    
    return l
    
N = int(input())
A = list(map(int, input().split()))
A.sort()
print(N-binary_search())