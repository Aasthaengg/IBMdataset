n = int(input())
A = list(map(int, input().split()))

sum_eve = sum(A[0::2])
sum_odd = sum(A[1::2])

x = [0] * n

x[0] = sum_eve - sum_odd

for num in range(1, n):
    x[num] = 2 * A[num-1] - x[num-1]
    
ans = " ".join(map(str,x))
print(ans)