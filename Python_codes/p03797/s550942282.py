N,M = map(int,input().split())
cnt = 0

m = int(M/2)

if N >= m:
    cnt = m
elif m > N:
    cnt = N
    M -= 2*N
    cnt += int(M/4)

print(cnt)