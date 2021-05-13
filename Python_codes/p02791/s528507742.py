a=int(input())
b=list(map(int,input().split()))
b_max=b[0]
total=0
for i in range(1,a):
    if b[i]<=b_max:
        total+=1
        b_max=b[i]
print(total+1)