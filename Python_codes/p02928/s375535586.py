n, k = map(int,input().split())
a_l = list(map(int,input().split()))
mod = 10**9+7

count1 = 0
for i in range(n):
    for j in range(i+1,n):
        if a_l[i] > a_l[j]:
            count1 += 1

a_l += a_l
count2 = 0
for i in range(n*2):
    for j in range(i+1,n*2):
        if a_l[i] > a_l[j]:
            count2 += 1
count2 -= count1*2

ans = count2*(k-1)*k//2 + count1*k
ans%=mod

print (ans)