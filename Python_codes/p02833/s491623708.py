N = int(input())
out=0

if N%2 ==1:
    out=0

else:
    k=5
    while k<10**18:
        out+= (N//k)//2
        k*=5

print(out)
