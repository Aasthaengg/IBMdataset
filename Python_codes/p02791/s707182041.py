n = int(input())
P = list(map(int,input().split()))

c=1
t=P[0]
for i in range(len(P)-1):
    if t>P[i+1]:
        c+=1
        t=P[i+1]

print(c)

        

