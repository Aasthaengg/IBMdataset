x = int(input())
ans = 0
for i in range(10**10):
    if i*(i+1)//2 >= x:
        ans = i
        break
print(ans)