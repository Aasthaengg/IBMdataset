N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))
num = abs(A - T + H[0]*0.006)
ans = 1
for i in range(1,N):
    if num > abs(A-T+H[i]*0.006):
        num = abs(A-T+H[i]*0.006)
        ans = i+1
print(ans)