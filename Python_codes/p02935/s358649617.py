N = int(input())
V = sorted(list(map(int,input().split())))
a = (V[0]+V[1])/2
for i in range(2,N):
    a = (a+V[i])/2
print(a)