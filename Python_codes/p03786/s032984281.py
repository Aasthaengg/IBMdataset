n=int(input())
a=sorted(list(map(int,input().split())))
flag=0
ans=1
a_cumulative=[0]
for i in range(n):
  flag+=a[i]
  a_cumulative.append(flag)
a.reverse()
a_cumulative.reverse()
for j in range(n-1):
  if a[j] <= a_cumulative[j+1]*2:
    ans+=1
  else:
    break
print(ans)