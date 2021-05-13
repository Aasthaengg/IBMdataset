n=int(input())
i=1
while True:
    if i**2<=n:
        i+=1
    else:
        i-=1
        break
print(i**2)