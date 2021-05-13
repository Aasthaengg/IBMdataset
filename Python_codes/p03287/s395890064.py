N, M = (int(i) for i in input().split())
A = [int(i) for i in input().split()]
 
D = [0] * (N + 1)
 
temp = 0
for i in range(N):
    temp = (A[i] + temp) % M
    D[i] = temp
#print(D)
D.sort()
#print(D)
temp = 0
cc = 1
for i in range(N):
    if D[i] == D[i + 1]:
        cc += 1
    else:
        temp += cc * (cc - 1) // 2
        cc = 1
temp += cc * (cc - 1) // 2
 
print(temp)