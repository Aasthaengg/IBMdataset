n,a,b = map(int,input().split())
if a % 2 == b % 2:
    print(abs(a-b)//2)
else:
    left = (a+b-1)//2
    right = (n*2-a-b+1)//2
    print(min(left,right))