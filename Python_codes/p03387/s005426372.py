a,b,c = sorted(map(int,input().split()))
if (b-a)%2==0:
    print(c-b+(b-a)//2)
else:
    print(c-b+1+(b-a+1)//2)