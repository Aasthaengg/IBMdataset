N=int(input())
A=input().split()
A=list(map(int,A))
def can_divide_by_2():
    for i in range(N):
        a=A[i]
        if a%2==0:
            a=a//2
            A[i]=a
        else:
            return False
for u in range(1000000):
    x=can_divide_by_2()
    if x==False:
        break
print(u)