n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ene = 0
for i in range(n):
    if b[i] >= a[i]+a[i+1]:
        ene += a[i]+a[i+1]
        a[i]=0
        a[i+1]=0
        #print("a1")
    elif b[i] >= a[i]:
        ene += b[i]
        a[i+1] -= b[i]-a[i]
        a[i]=0
        #print("a2")
    else:
        ene += b[i]
        a[i] -= b[i]
        #print("a3")
    #print(a)
print(ene)