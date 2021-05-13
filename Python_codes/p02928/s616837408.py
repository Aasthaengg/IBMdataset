n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10**9 + 7
def tentou(lis):
    res = 0
    for i in range(len(lis)-1):
        for j in range(i+1, len(lis)):
            if lis[i] > lis[j]:
                res += 1
    return res
x = tentou(a)
y = tentou(a+a) - 2*x
print((x*k%mod + y*k*(k-1)//2 %mod)%mod)