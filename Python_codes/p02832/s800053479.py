N = int(input())
a = list(map(int, input().split()))

num = 0
for item in a:
    if item == (num + 1):
        num += 1

if num != 0:
    print(N - num)
else:
    print(-1)
