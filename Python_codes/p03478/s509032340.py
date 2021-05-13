n,a,b=[int(i) for i in input().split()]

s_list=[]
for i in range(1,n+1):
    s=0
    x=i
    while True:
        if x//10!=0:
            s+=x%10
            x//=10
        else:
            s+=x%10
            break
    if a<=s<=b:
        s_list.append(i)

print(sum(s_list))  