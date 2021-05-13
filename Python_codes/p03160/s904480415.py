N = int(input())
h = list(map(int,input().split()))

ml = [10**9]* N

ml[0] = 0
ml[1] = abs(h[1]-h[0])
for i in range(2,N):
    ml[i] = min(abs(h[i]-h[i-1]) + ml[i-1], abs(h[i]-h[i-2]) + ml[i-2])

print(ml[N-1])
