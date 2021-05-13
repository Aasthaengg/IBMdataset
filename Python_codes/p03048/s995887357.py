R,G,B,N = map(int,input().split())
count = 0
for i in range(N+1):
    for j in range(N+1-i):
        a = N - i*R - j*G
        if a%B == 0 and a >= 0:
            count += 1
print(count)