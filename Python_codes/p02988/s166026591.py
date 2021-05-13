n = int(input())
P = list(map(int,input().split()))

c=0
for i in range(n-2):
    P2 = sorted(P[i:i+3])
    if P2[1]==P[i+1] :
        c+=1

print(c)