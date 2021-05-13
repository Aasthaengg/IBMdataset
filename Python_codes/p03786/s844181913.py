n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
sum_a = sum(a)

ans = n
for i in range(1,n):
    sum_a -= a[i-1]
    if a[i-1] <= 2*sum_a:
        pass
    else:
        print(i)
        exit()

print(n)