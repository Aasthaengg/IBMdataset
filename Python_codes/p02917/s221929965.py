n = int(input())
b = list(map(int,input().split()))

wa = 0

for i in range(n):
    if i == 0:
        wa += b[0]
    elif i == n-1:
        wa += b[n-2]
    else:
        wa += min(b[i-1],b[i])

print(wa)