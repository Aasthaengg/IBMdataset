n = int(input())
p = list(map(int, input().split()))

flg = 0
for num, val in enumerate(p):
    if (num + 1) != val:
        flg += 1
if flg == 2 or flg == 0:
    print("YES")
else:
    print("NO")