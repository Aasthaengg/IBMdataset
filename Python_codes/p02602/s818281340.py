N, K = map(int, input().split())
A = list(map(int, input().split()))
ACC = []
ACC.append(0)
sum = 0
for a in A:
    sum += a
    ACC.append(sum)


L = N-K+1
prev = ACC[K] - ACC[0]
for i in range(1, L):
    score = ACC[i+K] - ACC[i] 
    if prev < score:
        print("Yes")
    else:
        print("No")
    prev = score