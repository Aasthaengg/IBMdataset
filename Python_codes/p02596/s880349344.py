k = int(input())

ans = -1
x = 7%k
for n in range(1,k+10):
    if x == 0:
        ans = n
        break
    x = (10*x+7)%k
print(ans)