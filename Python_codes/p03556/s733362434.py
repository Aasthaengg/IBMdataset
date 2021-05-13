n=int(input())
max=0
for i in range(1,n+1):
    if i**2<=n:
        if i**2>max:
            max=i**2
    else:
        break
print(max)