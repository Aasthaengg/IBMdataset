n,k = map(int,input().split())
a = list(map(int,input().split()))
i = 1
while  n > k + (k-1)*(i-1):
    i += 1

print(i)

