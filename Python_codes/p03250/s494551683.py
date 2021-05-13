a = [int(i) for i in input().split()]
a.sort()
ans = ""
ans += str(a[-1])
ans += str(a[-2])
print(a[0] + int(ans))