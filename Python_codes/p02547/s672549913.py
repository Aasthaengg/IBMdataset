n = int(input())
ans = "No"
j = 0
for i in range(n):
  d,dd = map(str,input().split())
  if(d==dd):
    j += 1
  else:
    j=0
  if(j>=3):
    ans = "Yes"
print(ans)
