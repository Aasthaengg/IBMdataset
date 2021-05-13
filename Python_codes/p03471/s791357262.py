N,Y = map(int, input().split())
ans_10000= -1
ans_5000 = -1
ans_1000 = -1
for i in range(N+1):
    for j in range(N-i+1):
        if 10000*i+5000*j+1000*(N-i-j) == Y:
            ans_10000= i
            ans_5000 = j
            ans_1000 = N-i-j
            break
print(ans_10000, ans_5000, ans_1000)