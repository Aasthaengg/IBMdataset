k,t=map(int,input().split())
a=list(map(int,input().split()))
num=sum(a)-max(a)
if max(a)<=num+1:
    print(0)
else:
    if max(a)<=(num+1)*2:
        print(max(a)-(num+1))
    else:
        print(num+max(a)-num-1)
