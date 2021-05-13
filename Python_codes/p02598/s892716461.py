import sys , math

N,K=list(map(int, input().split()))
Ws=list(map(int, input().split()))
Ws.sort(reverse=True)

l=0
r=10**9

def check (m):
    now=0
    for i in range(N):
        now += (Ws[i] - 1) // m
    return now <= K

while r - l > 1:
    m = ( l + r ) // 2

    if check(m):
        r = m
    else:
        l = m
print(r) 