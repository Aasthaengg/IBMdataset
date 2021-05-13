# ABC073 C:Sentou
N,T = map(int, input().split())
l = list(map(int, input().split()))
x = T

for i in range(1,N):
    interv = l[i] - l[i-1]
    if interv < T:
        x += interv
    else:
        x += T
print(x)

