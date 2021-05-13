N = int(input())

for i in range(17):
    if 10**i <=N <10**(i+1):
        m=i+1
        break

for j in range(0,10):
    if (10**(m-1))*j + 10**(m-1)-1 <=N< (j+1)*(10**(m-1))+10**(m-1)-1:
        a = j
        break

print(a+9*(m-1))