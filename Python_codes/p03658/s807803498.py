n,k = list(map(int,input().strip().split()))
a = list(map(int,input().strip().split()))
a.sort(reverse=True)

print(sum(a[0:k]))