#17 C - Sentou
N, T = map(int,input().split())
t = list(map(int,input().split()))

time = 0
for i in range(1,N):
    diff = t[i] - t[i-1]
    if diff < T:
        time += diff
    else:
        time += T
print(time+T)   