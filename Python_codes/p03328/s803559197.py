import sys
a,b = map(int,input().split())
l = [(n*(n+1))//2 for n in range(1,1000)]
for i in range(len(l)-1):
  if l[i+1]-l[i] == b - a:
    print(l[i]-a)
    sys.exit()