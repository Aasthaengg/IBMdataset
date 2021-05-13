def mark(n):
    for i in range(n):
        num = int(input())
        if num in A:
            A[A.index(num)]=0

def tate():
    for i in range(3):
        if A[i]==A[i+3] and A[i]==A[i+6]:
            return 1
    return 0

def yoko():
    for i in range(0,7,3):
        if A[i]==A[i+1] and A[i]==A[i+2]:
            return 1
    return 0

def naname():
    if A[4]==A[0] and A[4]==A[8]:
        return 1
    elif A[4]==A[2] and A[4]==A[6]:
        return 1
    else:
        return 0

a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
a3=list(map(int,input().split()))
A=a1+a2+a3
n = int(input())
mark(n)
if tate()+yoko()+naname()>0:
    print("Yes")
else:
    print("No")