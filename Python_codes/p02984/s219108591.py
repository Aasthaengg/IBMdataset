n = int(input())
a = list(map(int, input().split()))
sum_a = sum(a)
a2 = 0 # 一番最初の値を求める X1 = total A - 1つずつ (最初以外は、ペアとなる(足してXになる)相手が存在する) 
for i in range(1, n, 2):
    a2 += a[i]
 
ans = [0] * n
ans[0] = sum_a - 2*a2
for i in range(1, n):
    ans[i] = 2*a[i-1] - ans[i-1] # 最初がわかれば、あとは漸化式 Xi + Xi+1 = 2Aiに沿って算出可能
print(*ans)