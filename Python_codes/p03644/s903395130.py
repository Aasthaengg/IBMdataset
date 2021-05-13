n=int(input())
for i in range(10):
    if 2**i>n:
        ans=i-1
        break
print(2**ans)