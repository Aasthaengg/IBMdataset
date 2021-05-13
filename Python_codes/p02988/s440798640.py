N = int(input())
P = list(map(int, input().split()))
c=0
for i in range(N-2):
    if P[i] < P[i+1] < P[i+2]:
        c += 1
    elif P[i] >  P[i+1] > P[i+2]:
        c+=1
print(c)