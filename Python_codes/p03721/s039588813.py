NMAX = 100005
n,k = map(int,input().split())

array = [0] * NMAX

for i in range(n):
    a,b = map(int,input().split())
    array[a] += b

for i in range(1,NMAX,1):
    if k <= array[i]:
        print(i)
        exit()
    k -= array[i]