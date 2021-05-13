n=int(input())
ans=[2,1]
if n in [0,1]:
  print(ans[n])
  quit()
for i in range(2,n+1):
  ans.append(ans[i-2]+ans[i-1])
print(ans[-1])