N = int(input())
T,A = map(int,input().split())
Hls = list(map(int,input().split()))
mabs = 10**5+1
for i in range(N):
    if abs(A-(T-Hls[i]*0.006)) <= mabs:
        mabs = abs(A-(T-Hls[i]*0.006))
        ans = i
    else:
        pass
print(ans+1)
