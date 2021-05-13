N = int(input())
x = 2
for i in range(100):
    if x**i > N:
        ans = x**(i-1)
        break
print(ans)
