n, k = map(int,input().split())
ans = 0
n_list = [i for i in range(n+1)]
l = sum(n_list[:k])
r = sum(n_list[len(n_list)-k:])
ans += r-l+1

for i in range(k,n+1):
    l += n_list[i]
    r += n_list[len(n_list)-i-1]
    ans += r-l+1
    ans = ans%1000000007

print(ans)
