n=int(input())
l=[]

for i in range(n):
  t=int(input())
  l.append(t)
# print(l)

def lcm(a,b):#最小公倍数
  ori_a=a
  ori_b=b
  while b!=0:
      a,b=b,a%b
  return (ori_a*ori_b)//a
  

ans=1
for i in l:
  ans=lcm(ans,i)

print(ans)