N = int(input())
A,B = map(int,input().split())
P = list(map(int,input().split()))

a = 0
b = 0
c = 0
for i in range(N):
    if P[i]<=A:
        a += 1
    elif P[i]<=B:
        b += 1
    elif B<P[i]:
        c += 1

print(min(a,b,c))