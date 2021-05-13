k, t = map(int, input().split())
a = list(map(int, input().split()))
num = max(a)
if (k + 1) // 2 >= num:
    print(0)
else:
    print(num * 2 - k - 1)