A,B=map(int,input().split())
c=0
for i in range(2):
    if A<B:
        c+=B
        B-=1
    else:
        c+=A
        A-=1
print(c)