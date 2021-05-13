N=int(input())
a=list(map(int,input().split()))
a=sorted(a)
a_set=sorted(list(set(a)))

flag=False
if sum(a)==0:
    flag=True
elif N%3==0:
    if len(a_set)==2:
        x,y=a_set
        if x==0 and a.count(x)*3==N:
            flag=True
    elif len(a_set)==3:
        x,y,z=a_set
        if x^y^z==0 and a.count(x)==a.count(y) and a.count(y)==a.count(z):
            flag=True

print('Yes' if flag else 'No')