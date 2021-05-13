n = int(input()) 
a = list(map(int,input().split()))

m = 10**6
cnt = 0
for i in range(n):
    if m >= a[i]:
        cnt += 1
        m = a[i]
print(cnt)
