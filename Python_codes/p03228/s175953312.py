abk=list(map(int,input().split()))
a=abk[0]
b=abk[1]
k=abk[2]
for i in range(k):
    if i%2 == 0:
        b = b + a//2
        a = a//2
    else:
        a = a + b//2
        b = b//2
print(a,b)
