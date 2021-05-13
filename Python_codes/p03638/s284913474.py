#17:24
h,w = map(int,input().split())
n = int(input())
c = list(map(int,input().split()))
ans1 = []
for i in range(n):
  ans1 += [i+1] * c[i]
ans2 = []
for x in range(h):
  ans2.append(ans1[w*x:w*(x+1)])
for x in range(h):
  if x % 2 == 1:
    ans2[x].reverse()
#print(ans1)
#print(ans2)
for x in range(h):
  print(' '.join(list(map(str,ans2[x]))))