N = int(input())
P = list(map(int, input().split())) 

cnt = 0
skip = False
for i in range(N):
    if skip:
        skip = False
        continue
    if i+1 == P[i]:
        cnt += 1
        if i+1 < N and i+2 == P[i+1]:
            skip = True

print(cnt)
