import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))

abs1 = [0]*(n-1)
abs1_sum = 0
for i in range(1,n):
    abs1[i-1] = abs(a[i-1]-a[i])
    abs1_sum += abs(a[i-1]-a[i])


abs2 = [0]*(n-2)
for i in range(2,n):
    abs2[i-2] = abs(a[i-2]-a[i])
#print(abs1)

b_0 = abs(a[0])
b_1 = abs(a[1])
b_n1 = abs(a[n-1])
b_n2 = abs(a[n-2])
ans = []
for i in range(n):
    if i == 0:
        ans.append(abs1_sum - abs1[0] + b_1 + b_n1)
    elif i == n-1:#
        #print(abs1[:n-2],abs(p[0]),abs(p[-1]))
        ans.append(abs1_sum - abs1[-1] + b_0 + b_n2)
    else:
        ans.append(b_0 + b_n1 + abs1_sum - abs1[i] - abs1[i-1] + abs2[i-1])

for i in range(n):
    print(ans[i])


