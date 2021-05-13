n = int(input())
a=list(map(int,input().split()))

odd=[0]*n
j=0

for i in a:
    while i%2==0:
        odd[j]+=1
        i//=2
    j+=1
print(sum(odd))