n = int(input())
k = int(input())
x = int(input())
y = int(input())
print(sum([x if i<=k else y for i in range(1,n+1)]))