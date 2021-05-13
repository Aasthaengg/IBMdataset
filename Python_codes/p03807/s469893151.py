n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in a:
    if i % 2 == 1:
        cnt += 1
if n == 1 or cnt % 2 == 0:
    print("YES")
else:
    print("NO")
