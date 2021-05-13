n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
a.sort()

result = a[0][0] -(a[0][0] - 1) + (a[n-1][1]) +(a[n-1][0]) -1
print(result)