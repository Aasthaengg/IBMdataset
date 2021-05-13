N = int(input())
lis = list(map(int, input().split()))

cnt = 0

for i in range(N):
    if lis[i] == i+1:
        cnt += 1


if N-2 <= cnt:
    print("YES")
else:
    print("NO")
