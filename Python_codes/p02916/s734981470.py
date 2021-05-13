_ = input()
a = [int(e) for e in input().split(" ")]
b = [int(e) for e in input().split(" ")]
c = [int(e) for e in input().split(" ")]
res = 0
for i,j in enumerate(a):
  res += b[j-1]
  if i != 0 and j - a[i-1] == 1:
    res += c[j-2]
print(res) 