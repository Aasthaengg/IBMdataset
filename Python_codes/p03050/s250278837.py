N = int(input())
A = []
for i in range(1,int(N**0.5)+1):
    if N%i==0:
        a = i
        b = N//i
        if a>b:
            a,b = b,a
        if 0<a<b-1:
            A.append(b-1)
print(sum(A))