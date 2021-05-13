N=int(input())

m = -1
ans = None
for i in range(N):
    j = i+1
    sum = 0
    while True:
        if j%2 == 0:
            j //= 2
            sum+=1
        else:
            break
    if sum > m:
        m = sum
        ans = i+1

print(ans)