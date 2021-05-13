A,B,C = map(int,input().split())
x = [0,0,0]
K = int(input())
flag = False
for i in range(K+1):
    for j in range(K+1):
        for k in range(K+1):
            x = A*(2**i)
            y = B*(2**j)
            z = C*(2**k)
            if i+j+k<=K and x<y and y<z:
                flag = True
                break
if flag == True:
    print("Yes")
else:
    print("No")