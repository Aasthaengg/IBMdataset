a=input()
n=len(a)
if n<5 or n>10:
    print('NO')
    exit()

for i in range(2**(n+1)):
    s=""
    check=[""]*(n+1)
    for j in range(n+1):
        if ((i>>j)&1):
            check[j]="A"
    for k in range(n+1):
        s+=check[k]
        if k!=n:
            s+=a[k]
    if s=="AKIHABARA":
        print('YES')
        exit()
print('NO')