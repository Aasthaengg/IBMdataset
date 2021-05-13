# 085 C
N,Y = map(int, input().split())
x,y,z = -1,-1,-1
for i in range(N+1):
    for j in range(N+1):
        if ((10000*i + 5000*j + 1000*(N-i-j)) == Y)and(N-i-j>=0):
            x,y = i,j
            z = N - i - j
            break
    else:
        continue
    break
print(x,y,z)            