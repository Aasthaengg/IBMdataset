n = int(input())
ans = n
i = 1
while i*i<=n :
  if n%i == 0 :
    d = n//i
    if ans > i+d-2 : ans = i+d-2
  i+=1
print(ans)
