N = int(input())
d = list(map(int, input().split()))

d.sort()

s = d[N//2-1]
e = d[N//2]
K = e - s 
print(K)