N=int(input())

A=input()
B=input()
C=input()

list=[]
for i in range(N):
    a=A[i]
    b=B[i]
    c=C[i]

    if a==b and b==c:
        list.append(0)
    elif (a==b and b!=c) \
        or (a==c and a!=b) \
        or (b==c and a!=c):
        list.append(1)
    elif a!=b and b!=c and c!=a:
        list.append(2)

print(sum(list))