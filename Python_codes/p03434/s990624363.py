#Card Game for Two
a=int(input())
b=list(map(int,input().split()))
b.sort()
total=0
total2=0
for i in range(a):
    if i%2==0:
        total+=b[i]
    else:
        total2+=b[i]
print(max(total,total2)-min(total,total2))