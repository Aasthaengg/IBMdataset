R,G,B,N = map(int,input().split())
c = 0
for i in range(3001):
    for j in range(3001):
        if R*i+G*j > N:
            continue
        if (N - (R*i+G*j)) % B == 0:
            c+= 1
print(c)
