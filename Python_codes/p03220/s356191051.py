n = int(input())
t, a = map(float,input().split())
h = list(map(int,input().split()))
l = []
j = 0

for i in range(n):
    l.append(abs(a-(t-h[j]*0.006)))
    j+=1

maxv = min(l)
print(l.index(maxv)+1)
