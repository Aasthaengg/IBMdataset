N=int(input())

if N==0:
    print(0)
    exit()

S=""
while N:
    S=str(N%2)+S
    N=-(N-(N%2))//2
print(S)