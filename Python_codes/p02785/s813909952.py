n,k=map(int,input().split())
h=list(map(int,input().split()))

h.sort(reverse=True)

if k>n:
  k=n

for i in range(k):
  h[i]=0

sum_=0
for hh in h:
  sum_+=hh
print(sum_)