n=int(input())
for i in range(1,10**9):
    if i*i > n:
        break
print((i-1)*(i-1))