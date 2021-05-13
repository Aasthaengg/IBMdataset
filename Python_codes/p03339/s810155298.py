n = int(input())
s = input()
dp=[0]*(n)
dp[0] = s[1:].count("E")
for i in range(1,n):
  temp=dp[i-1]
  if s[i-1] == "W":
    temp+=1
  if s[i] == "E":
    temp-=1
  
  dp[i]=temp

print(min(dp))