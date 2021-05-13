k = int(input())
a = list(map(int,input().split()))
a = a[::-1]
ansmin = 2
ansmax = 2
for i in range(k):
  x = a[i]
  ansmin = x*((ansmin+x-1)//x)
  ansmax = x*(ansmax//x)+x-1
  if ansmin>ansmax:
    print(-1)
    exit()
print(ansmin,ansmax)