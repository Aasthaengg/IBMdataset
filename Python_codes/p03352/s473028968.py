X=int(input())

M=1
for b in range(2,X+1):
    if b*b<=X:
        a=b*b
        while a*b<=X:
            a*=b
        M=max(M,a)

print(M)
