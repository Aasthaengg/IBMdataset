n = int(input())
a = [int(i) for i in input().split()]
a.append(a[0])
s = 0
for i in a: s ^= i
ans = "Yes" if s == a[0] else "No"
print(ans)