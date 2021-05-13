n = int(input())
S = input().split()

q = int(input())
T = input().split()

cnt = 0

for i in range(q):
    if T[i] in S:
        cnt += 1

print(cnt)