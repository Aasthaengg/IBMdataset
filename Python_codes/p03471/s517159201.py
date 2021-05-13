N, Y = map(int,input().split())

a1 = -1
b1 = -1
c1 = -1
for i in range(N+1):
    for j in range(N+1-i):
        total = 10000*i+5000*j+1000*(N-i-j)
        if total == Y:
            a1 = i
            b1 = j
            c1 = N-i-j

print(str(a1)+" "+str(b1)+" "+str(c1))
        
