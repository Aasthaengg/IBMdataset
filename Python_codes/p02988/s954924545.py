n=int(input())
P=list(map(int,input().split()))
count=0
for i in range(n-2):
    if P[i+1]!=max(P[i:i+3]) and P[i+1]!=min(P[i:i+3]):
        count+=1
print(count)