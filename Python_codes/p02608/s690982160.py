N = int(input())
a = [0]*10050
for i in range(1,100):
    for j in range(1,100):
        for k in range(1,100):
            v = i*i+j*j+k*k+i*j+i*k+j*k
            if v <= 10000:
                a[v-1] += 1

for i in range(N):
    print(a[i])
