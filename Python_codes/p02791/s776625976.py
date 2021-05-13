N = int(input())
P = list(map(int,input().split()))
x = P[0]
a = 1
for i in range(N-1):
    if x >= P[i+1] :
        a+=1
        x=P[i+1]
print(a)
    

