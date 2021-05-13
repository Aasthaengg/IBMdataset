a=int(input())
b=list(map(int,input().split()))
c=int(sum(b)/len(b)+0.5)
total=0
for i in range(a):
    total+=(b[i]-c)**2
print(total)