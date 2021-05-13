N = int(input())
A = list(map(int,input().split()))
B = [A[i]-i-1 for i in range(N)]
B.sort()

ave = B[N//2]
ans = 0
for i in range(N):
    ans += abs(B[i]-ave)
print(ans)