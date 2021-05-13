n = int(input())

if n % 2 == 0:
    nn = n
    print(n*(n-2)//2)
else:
    nn = n-1
    print(nn*(nn-2)//2+nn)



for i in range(1,nn//2):
    for j in range(i+1,nn//2 + 1):
        print(i,j)
        print(i,nn+1-j)
        print(nn+1-i,j)
        print(nn+1-i,nn+1-j)

if n % 2 == 1:
    for i in range(1,n):
        print(i,n)