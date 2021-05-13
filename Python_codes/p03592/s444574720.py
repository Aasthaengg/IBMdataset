n,m,k= input().split()

n = int(n)
m = int(m)
k = int(k)

for i in range(n+1):
    for j in range(m+1):
        if k == (i*(m-j) + (n-i)*j) :
            print("Yes")
            exit()


print("No")
