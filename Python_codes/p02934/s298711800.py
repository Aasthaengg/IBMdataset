n=int(input())
li=list(map(int,input().split()))
m=0
for i in li:
    m+=1/i
print(1/m)