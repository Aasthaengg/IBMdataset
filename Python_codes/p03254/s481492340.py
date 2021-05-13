n, x = map(int, input().split())
a = list(map(int, input().split()))

l = sorted(a)
flag = False
for i in range(n):
    x -= l[i]
    if x < 0:
        flag = True
        break
if flag:
    print(i)
elif x == 0:
    print(n)
elif x > 0:
    print(n - 1)
