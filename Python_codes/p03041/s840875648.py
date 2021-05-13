n,k = map(int, input().split())
s = input()

k = k-1

for i in range(n):
  if i == k:
    x = s[i].lower()
    print(x,end="")
  else:
    print(s[i],end="")
