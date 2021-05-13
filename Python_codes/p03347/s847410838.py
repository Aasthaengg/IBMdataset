import sys
input = sys.stdin.readline

def calc(l):
    l2 = l[::-1]
    res = l2[0]
    
    for i in range(1, len(l2)):
        if l2[i-1]-1>l2[i]:
            print(-1)
            exit()
            
        if l2[i]!=l2[i-1]-1:
            res += l2[i]

    return res

N = int(input())
A = [int(input()) for _ in range(N)]

for i in range(N):
    if A[i]>i:
        print(-1)
        exit()

ans = 0
l = []

for i in range(N):
    if i==N-1 or A[i]>A[i+1]:
        l.append(A[i])
        ans += calc(l)
        l = []
    else:
        l.append(A[i])

print(ans)