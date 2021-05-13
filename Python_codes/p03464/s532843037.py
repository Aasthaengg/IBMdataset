k = int(input())
a = [int(i) for i in input().split()]
l = r = 2
for i in reversed(a):
    if (l - 1) // i == r // i:
        print(-1)
        break
    l, r = (l + i - 1) // i * i, r // i * i + i - 1
else:
    print(l, r)
