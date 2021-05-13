n=int(input())
s=[int(input()) for i in range(n)]
s.sort()

ans=sum(s)
if ans%10!=0:
  print(ans)
  exit()

t_ans=ans
for i in range(n):
  t_ans-=s[i]

  if t_ans%10!=0:
    print(t_ans)
    exit()

  i+=1
  t_ans=ans

print(0)