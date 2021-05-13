N = int(input())

lucas = (N+2)*[0]
lucas[0] = 2
lucas[1] = 1
for i in range(2,N+2):
    lucas[i] = lucas[i-1]+lucas[i-2]

print(lucas[N])