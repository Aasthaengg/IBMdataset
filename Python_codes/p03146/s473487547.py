s=int(input())
a=[s]
check=0
for i in range(1000000):
    n=a[i]
    if n%2==0:
        num=n//2
        if num in a:
            check=i+2
            break
        a.append(num)
    else:
        num=3*n+1
        if num in a:
            check=i+2
            break
        a.append(num)
print(check)
#print(*a)