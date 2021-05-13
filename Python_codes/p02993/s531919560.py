s = str(input())
ans = "Good"
for i in range(10):
  k = str(i)+str(i)
  if(k in s):
    ans = "Bad"
    break
print(ans)
