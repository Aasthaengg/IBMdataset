n = int(input())

p = list(map(int,input().split()))

c = 0
for i in range(n-1):
    if(p[i] == i+1 and p[i+1] == i+2):
        p[i],p[i+1] = p[i+1],p[i]
        c += 1
for i in range(n):
    if(p[i] == i+1):c += 1
print(c)
