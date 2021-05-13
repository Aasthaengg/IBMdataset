s = input()
prev = s[0]
n = len(s)
cnt= 0
L = [0]*(n+1)
R = [0]*(n+1)
for i in range(n):
    if s[i] =="<":
        cnt+=1
    else:
        cnt=0
    L[i+1] = cnt
s= s[::-1]
for i in range(n):
    if s[i] ==">":
        cnt+=1
    else:
        cnt=0
    R[i+1] = cnt
ans = 0
for i in range(n+1):
    ans+=max(L[i],R[-i-1])
print(ans)
