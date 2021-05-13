N = int(input())
for i in range(1,10):
    if N < 2**i:
        ans = 2**(i-1)
        break
print(ans)