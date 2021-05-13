#3 
N = int(input())
answer = [0]*N
for k in range(1, int(N**(1/2))):
    for l in range(1, int(N**(1/2))):
        for m in range(1, int(N**(1/2))):
            v = k**2 + l**2 + m**2 + k*l + l*m + m*k
            if v-1 < N:
                answer[v-1] += 1
for i in range(N):
    print(answer[i])