N, K = map(int, input().split())
A = list(map(int, input().split()))
zero_count = [0 for i in range(50)]
for x in A:
    for i in range(50):
        zero_count[i] += 1 - (x >> i) & 1

ans = sum(A)
res = 0
for x in A:
	res+= (K^x)
ans =max(ans,res)    
K_bit_1 = [False for i in range(50)]
for i in range(49, -1, -1):
    if K >> i & 1:
        K_bit_1[i] = True

for x in range(50):
    if K_bit_1[x] == True:
        sub_ans = 0
        for i in range(49, x, -1):
            if K_bit_1[i]:
                sub_ans += (zero_count[i])*(1 << i)
            else:
                sub_ans += (N-zero_count[i])*(1 << i)
        sub_ans += (N-zero_count[x])*(1 << x)
        for j in range(x-1, -1, -1):
            sub_ans += max(N-zero_count[j], zero_count[j])*(1 << j)
        ans = max(sub_ans, ans)
print(ans)
