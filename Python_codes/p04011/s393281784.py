N = int(input())
K = int(input())
X = int(input())
Y = int(input())
m=0
for i in range(1,N+1):
    if i<=K:
        m+=X
    else:
        m+=Y

print(m)