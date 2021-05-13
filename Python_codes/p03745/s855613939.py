import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
ans = 0
state = 0

for i in range(N-1):
    if A[i+1]-A[i]>0:
        if state==2:
            ans += 1
            state = 0
        elif state==0:
            state = 1
    elif A[i+1]-A[i]<0:
        if state==1:
            ans += 1
            state = 0
        else:
            state = 2

ans += 1
print(ans)