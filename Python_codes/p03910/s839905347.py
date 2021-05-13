#97 B - Exactly N points
N = int(input())

A = []
num = 1
cnt = 0
for _ in range(N):
    A.append(num)
    cnt += 1
    if num == cnt:
        cnt = 0
        num += 1

ans = [A[-1]]
tgt = N - A[-1]

for i in range(A[-1]-1,0,-1):
    tgt -= i
    if tgt == 0:
        ans.append(i)
        break
    if tgt < 0:
        tgt += i
        continue
    ans.append(i)

for a in ans:
    print(a)