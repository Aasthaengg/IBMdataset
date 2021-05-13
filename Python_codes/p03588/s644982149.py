n = int(input())
a = []
for i in range(n):
  a.append(list(map(int, input().split())))
a.sort(reverse=True)
print(a[0][0] + a[0][1])