n,m=map(int,input().split())
num=[int(i) for i in input().split()]
num=sorted(num,reverse=True)
sum_num=sum(num)
if num[m-1]<sum_num/(4*m):
    print("No")
else:
    print("Yes")
