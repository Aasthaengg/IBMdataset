N = int(input())
a = [int(i) for i in input().split()]
a.sort(reverse=True)

ans = sum(a[2*i-1] for i in range(1,N+1))
print(ans)