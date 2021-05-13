n=int(input())
s=input()
s_l=len(s)

ans=0
for i in range(s_l):
  set1=set(s[:i])
  set2=set(s[i:])
  t_ans=len(set1&set2)
  ans=max(ans,t_ans)
print(ans)