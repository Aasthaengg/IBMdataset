N,M = map(int,input().split())
k = 0
t = 0
j = 0
before = N
for i in range(1,M+1):
    if N - before + i == N//2 and N%2 == 0:
        j = 1
    else:
        if N - before + t + i == k:
            t = 1
        k = before - t - i
        print(i,before-t)
        before -= 1
if j == 1:
    i += 1
    print(i,before-t)