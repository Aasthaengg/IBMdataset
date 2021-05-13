n = int(input())
for i in range(1,8):
    if n == i:
        ans = 1
        break
    if 2**i > n:
        ans =2**(i-1)
        break
print(ans)