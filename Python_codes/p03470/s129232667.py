# input
N = int(input())
D = [int(input()) for i in range(N)]

# check
cnt = 0
while len(D) > 0:
    max_d = max(D)
    D = [d for d in D if d < max_d]
    cnt += 1

print(cnt)
