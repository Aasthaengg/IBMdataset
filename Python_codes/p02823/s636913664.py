n,a,b = map(int, input().split())
if (b-a)%2 == 0:
    print((b-a)//2)
    exit()
if (n-b) <= (a-1):
    print(n-b+(b-a)//2+1)
    exit()
print(a-1+ (b-a)//2+1)
