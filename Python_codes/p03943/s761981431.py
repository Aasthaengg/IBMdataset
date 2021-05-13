l = list(map(int, input().split()))
s = sum(l)
m = s / 2
if m in l:
    print("Yes")

else:
    print("No")