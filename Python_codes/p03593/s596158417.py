from collections import Counter 

a,b = map(int,input().split())
l = ''
for i in range(a):
    t = input()
    l+=t

c = Counter(list(l))
# print(c)
dp = [0,0,0]
for i in c:
    if c[i]%2 ==1:
        dp[0] +=1
    elif c[i]%4 == 0:
        dp[2] += 1
    elif c[i]%2 == 0:
        dp[1] += 1
# print(dp)
ans = 'No'
if a%2 ==1 and b%2 ==1:
    A = 1
    B = (a+b-2)//2
    if A >= dp[0] and B >= dp[1]:
        ans = 'Yes'
elif  a%2 ==0 and b%2 ==0:
    A = 0
    B= 0
    if A >= dp[0] and B >= dp[1]:
        ans = 'Yes'
elif a%2 ==0 and b%2 ==1:
    A = 0
    B = a//2
    if A >= dp[0] and B >= dp[1]:
        ans = 'Yes'
else:
    A=0
    B= b//2
    if A >= dp[0] and B >= dp[1]:
        ans = 'Yes'
print(ans)
