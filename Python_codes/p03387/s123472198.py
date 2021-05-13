D = sorted(list(map(int,input().split())))
A,B,C = D
if (C-B)%2==0 and (B-A)%2==0:
    n = (C-B)//2+(C-A)//2
elif (C-B)%2==1 and (B-A)%2==0:
    n = (B-A)//2+(C-B)
elif (C-B)%2==0 and (B-A)%2==1:
    n = (C-B)//2+1 +(C+1-A)//2
elif (C-B)%2==1 and (B-A)%2==1:
    n = 1+(C-B-1)//2+1+(C-A)//2
print(n)