import sys
n,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
start = 0
end = k
count = 0
for i in range(n):
    if a[n-1]==1:
        print(count)
        sys.exit()
    a[start:end] = [1]*k
    start += (k-1)
    end += (k-1)
    count += 1