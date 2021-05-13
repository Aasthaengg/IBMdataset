from bisect import bisect_left as b
n,m= map(int,input().split())
a=list(map(int,input().split()))
a.sort()
while m>0:
  i=a.pop(-1)//2
  a.insert(b(a,i),i)
  m-=1
print(sum(a))