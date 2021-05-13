N = int(input())
A = []
B = []
for i in range(2,int(N**0.5)+1):
    if N%i==0:
        A.append(i)
        A.append(N//i)
    if (N-1)%i==0:
        B.append(i)
        B.append((N-1)//i)
A.append(N)
if N>2:
    B.append(N-1)
A = sorted(A)
for a in A:
    m = 1
    while True:
        if a**m==N:
            B.append(a)
            break
        elif a**m>N:
            break
        m += 1
for a in A:
    m=0
    while a**m<N:
        if N%a**m==0:
            if (N//(a**m)-1)%a==0:
                B.append(a)
        m += 1
B = sorted(list(set(B)))
print(len(B))