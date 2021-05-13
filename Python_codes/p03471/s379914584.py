i = [int(i) for i in input().split()]
N = i[0]
Y = i[1]

# 10000*N - Y = 5000*y + 9000*z
# 10*N - Y/1000 = 5*y + 9*z
sum = 10*N - Y/1000
for y in range(N+1):
    for z in range(N-y+1):
        if sum == 5*y + 9*z:
            print(str(N-y-z) + " " + str(y) + " " + str(z))
            exit()
print("-1 -1 -1")