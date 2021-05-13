d, n=map(int, input().split())
k=100**d

if n==100:
    num="101"+2*d*"0"
    num=int(num)
    print(num)
else:
    print(k*n)