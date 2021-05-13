N,M = map(int, input().split())
Key = [0 for i in range(N+1)]
for _ in range(M):
    L,R = map(int,input().split())
    L -= 1
    R -= 1
    Key[L] += 1
    Key[R+1] -= 1
count = 0
sum = 0
for i in range(len(Key)):
    sum += Key[i]
    if sum == M:
        count += 1
print(count)