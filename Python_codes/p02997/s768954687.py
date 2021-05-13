n, k = [int(x) for x in input().strip().split(" ")]
m=~-n*(n-2)//2
if k>m:
    print(-1)
else:
    m-=k
    print(m+n-1)
    for i in range(1, n):
        print(i, n)
    for i in range(1, n):
        for j in range(i+1, n):
            if m==0:
                break
            print(i, j)
            m-=1
