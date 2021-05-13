n=int(input())
ab=[]
for i in range(n):
  aa,bb=map(int,input().split())
  ab.append((aa,bb))
t_sum=0
ab=ab[::-1]
for a,b in ab:
  if (a+t_sum)%b!=0:
    t=b-(a+t_sum)%b
    t_sum+=t
print(t_sum)

