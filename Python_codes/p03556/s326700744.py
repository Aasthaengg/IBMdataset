N = int(input())
ans = 1
for i in range(1,31623):
    if N >= i**2:
        ans = i**2
    else:
        break
print(ans)