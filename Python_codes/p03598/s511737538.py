n = int(input())
k = int(input())
l = list(map(int, input().split()))
s = 0
for i in l:
  s += min(i, k - i)

print(2*s)