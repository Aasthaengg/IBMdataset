N = int(input())
A = list(map(int,input().split()))
B = [A[i]-i-1 for i in range(N)]
B.sort()

ave1,ave2 = B[N//2],B[N//2-1]
ans1,ans2 = 0,0
for i in range(N):
    ans1 += abs(B[i]-ave1)
    ans2 += abs(B[i]-ave2)
print(ans1)