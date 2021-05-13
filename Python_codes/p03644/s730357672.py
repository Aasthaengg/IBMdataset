N = int(input())
for n in range(7):
    if 2 ** n <= N:
        ans = 2 ** n
print(ans)