N = int(input())

SP =[]
for i in range(N):
    SP.append([i+1] + list(map(str,input().split())))
    SP[i][2] = int(SP[i][2])

SP = sorted(SP,key = lambda x: x[2], reverse=True)
SP = sorted(SP,key = lambda x: x[1])

for i in range(N):
    print(SP[i][0])
