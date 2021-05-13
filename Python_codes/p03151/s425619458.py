N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = [0] * N
neg = []
pos = []
for i in range(N):
    diff[i] = A[i] - B[i]
    if diff[i] < 0:
        neg.append(diff[i])
    else:
        pos.append(diff[i])

if sum(diff) < 0:
    print(-1)
    exit(0)

tobe_supplied = sum(neg)
pos.sort(reverse=True)

cnt = len(neg)

for p in pos:
    if tobe_supplied >= 0:
        break
    cnt += 1
    tobe_supplied += p    

print(cnt)