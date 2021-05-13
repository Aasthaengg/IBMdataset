n=int(input())
a=n//4
b=n//7
for i in range(a+1):
    for j in range(b+1):
        if 4*i+7*j==n:
            print("Yes")
            break
    else:
        continue
    break
else:
    print("No")