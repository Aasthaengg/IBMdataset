n,a,b=map(int, input().split())
ans_list=[]

for i in range(1,n+1):
    num=i
    re=0
    while num>0:
        re+=num%10
        num//=10
    if a<=re<=b:
        ans_list.append(i)

print(sum(ans_list))
