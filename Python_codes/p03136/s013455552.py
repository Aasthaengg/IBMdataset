n = int(input())
a = list(map(int, input().split()))
asum = sum(a)
amax = max(a)
if amax < asum-amax:
    print("Yes")
else:
    print("No")