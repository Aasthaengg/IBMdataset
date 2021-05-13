n,a,b = map(int,input().split())

if (b-a)%2 == 0:
    print((b-a)//2)
    exit()

print(min(b,n-a+1,a+(b-a)//2,n-b+1 + (b-a-1)//2) )