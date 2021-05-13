z = input()
s = int(input())
b, c = 0,0
r=[]
for i in range(s):
    a = input().split()
    if a[0] == "print":
        b, c = int(a[1]), int(a[2])
        print(z[int(b):int(c)+1])
    elif a[0] == "reverse":
        b, c = int(a[1]), int(a[2])
        r= list(z[b:c+1])
        r=r[::-1]
        z=list(z)
        z[b:c+1]=r
        z=''.join(z)

    else:
        b, c, d = int(a[1]), int(a[2]), list(a[3])
        z=list(z)
        z[b:c+1]=d
        z=''.join(z)