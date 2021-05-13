#B
n = int(input())
l = list(map(int, input().split()))
lmax = max(l)
l.sort(reverse=True)
if lmax < sum(l[1:]):
    print("Yes")
else:
    print("No")