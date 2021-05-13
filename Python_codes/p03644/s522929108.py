n=int(input())
res=1
for i in range(n):
    x=2**i
    if x>n:
        res=2**(i-1)
        break
print(res)