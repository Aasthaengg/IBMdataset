A=input()
dp=[0]*26
r=0
for i,a in enumerate(A):
    c=ord(a)-97
    r+=i-dp[c]
    dp[c]+=1
print(r+1)