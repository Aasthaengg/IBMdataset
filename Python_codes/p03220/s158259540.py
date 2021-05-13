N=int(input())
T,A=map(int,input().split())
H=list(map(int,input().split()))
min = 1e8
ans = None

for i in range(N):
    temp = T - H[i]*0.006
    diff = abs(A-temp)
    if diff < min:
        min = diff
        ans = i

print(ans + 1)