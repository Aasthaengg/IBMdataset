c=0
n=int(input())
ar=[int(i) for i in input().strip().split(" ")]
for i in range(n):
    t=ar[i]
    while(t%2==0):
        c+=1
        t=(t//2)
print(c)
