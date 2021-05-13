s,t=input().split()
a,b=map(int,input().split())
u=input()
dict={s:a,t:b}
if s==u:
  dict[s]-=1
else:
  dict[t]-=1
print(dict[s],dict[t])