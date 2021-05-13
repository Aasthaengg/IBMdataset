#d
n = int(input())
a = list(map(int, input().split()))
ans = [0]*n

d_sum = sum(a[1:-1:2])

ans[0] = sum(a)-(2*d_sum)

for i in range(1,len(a)):
    ans[i] = 2*a[i-1] -ans[i-1]

ans=[str(a) for a in ans]
ans=" ".join(ans)
print(ans)