N,M,K = map(int, input().split())
As = [int(n) for n in input().split()]
Bs = [int(n) for n in input().split()]

a_sum = [0]
b_sum = [0]

for i in range(len(As)):
    a_sum.append(a_sum[-1] + As[i])

for j in range(len(Bs)):
    b_sum.append(b_sum[-1] + Bs[j])

 
max_book_num = 0
j = M
for i in range(N+1):
    if a_sum[i] > K:
        continue

    while b_sum[j] + a_sum[i] > K:
        j -= 1
    
    max_book_num = max(max_book_num, i + j)

        
print(max_book_num)    

