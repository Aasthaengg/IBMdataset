d = []
a=int(input())
b = list(map(int,input().split()))
c = sum(b)/a
for i in b:
  d.append(abs(c - i))
e = min(d)
print(d.index(e))