x,a,b=map(int,input().split())
ad=abs(x-a)
bd=abs(x-b)

if ad > bd:
    print("B")
elif ad < bd:
    print("A")