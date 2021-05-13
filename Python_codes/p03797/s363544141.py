n,m = map(int,input().split())

if n*2 == m:
    print(n)
elif m < n*2 :
    print(m//2)
else :
    print(n+(m-n*2)//4)