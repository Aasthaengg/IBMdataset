num=list(map(int, input().split()))
num.sort()

m=num[2]*3

if sum(num)%2==m%2:
    print((m-sum(num))//2)
else:
    print((m-sum(num))//2+2)
