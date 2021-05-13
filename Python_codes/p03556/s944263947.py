N = int(input())
ans = 0
for i in range(1,100000):
    if i**2 > N:
        print(ans)
        exit()
    ans = i**2
print(ans)
