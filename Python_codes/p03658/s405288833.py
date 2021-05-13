n, k = input().split()
l = input().split()
L = []
for hoge in l:
  L.append(int(hoge))
L.sort()
L.reverse()
sum = 0
for i in range(int(k)):
  sum += L[i]
print(sum)