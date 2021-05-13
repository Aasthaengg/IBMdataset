N,K = map(int,input().split(" "))
sum = (N//K) ** 3

if K % 2 == 0:
    k = K // 2
    sum += ((N+k)//K) * (((N+K-k)//K)**2)

print(sum)