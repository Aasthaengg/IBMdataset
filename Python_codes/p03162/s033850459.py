# coding: utf-8
n = int(input())
dp1 = [0] * n
dp2 = [0] * n
dp3 = [0] * n
#print(dp1)
a, b, c = map(int,input().split())
dp1[0] = a
dp2[0] = b
dp3[0] = c
for i in range(1,n):
    a, b, c = map(int,input().split())
    dp1[i] = max(dp2[i-1]+a, dp3[i-1]+a)
    dp2[i] = max(dp1[i-1]+b, dp3[i-1]+b)
    dp3[i] = max(dp2[i-1]+c, dp1[i-1]+c)
print(max(dp1[n-1], dp2[n-1], dp3[n-1]))