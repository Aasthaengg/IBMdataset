import math

n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
b = [a[2*i+1] for i in range(n)]
print(sum(b))