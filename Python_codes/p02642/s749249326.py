N = int(input())
A = list(map(int, input().split()))
l = max(A)+1
li = [0]*(l)
A.sort()

for a in A:
  if li[a] == 0:
    li[a] = 1
    for i in range(a*2, l, a):
      li[i] = 2
  elif li[a] == 1:
    li[a] = 2
print(li.count(1))
