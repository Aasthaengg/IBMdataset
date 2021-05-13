n = int(input())
a_li = list(map(int,input().split()))
a_sum = sum(a_li)
num = 0
ans = 10**10
for i in range(n-1):
    num += a_li[i]
    ans = min(abs(a_sum-num-num),ans)
print(ans)
