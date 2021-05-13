N = int(input())
As = [int(input()) for i in range(N)]

cnt = 0
for a in As:
    if a % 2 == 0:
        cnt += 1
if cnt == N:
    print("second")
else:print("first")
