n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
print(sum(max(a[n:2*n], [a[2*i+1] for i in range(n)])))