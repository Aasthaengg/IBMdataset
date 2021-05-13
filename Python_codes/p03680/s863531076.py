N = int(input())
a = [int(input()) for _ in range(N)]
 
i = 0
m = 1
while(1):
    if a[i] == 2:
        ans = m
        break
 
    if m >= N:
        ans = -1
        break
 
    i = a[i] - 1 
    m += 1

print(ans)