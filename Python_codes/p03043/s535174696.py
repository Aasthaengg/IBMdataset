N,K = map(int,input().split())

def div_count(n,i):
    ans = i
    count = 0
    while n>ans:
        ans *= 2
        count += 1
    return count
ans = 0
for i in range(1,N+1):
    count = div_count(K,i)
    ans += (1/N) * pow(0.5,count)
print(ans)





