n = int(input())
a = list(map(int, input().split()))
print(sum([a[i]%2 for i in range(0,n,2)]))