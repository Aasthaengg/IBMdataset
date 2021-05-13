from bisect import bisect_left, bisect_right
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ruisekiwa_of_A = [0]
ruisekiwa_of_B = [0]
for a in A:
    ruisekiwa_of_A.append(ruisekiwa_of_A[-1]+a)
for b in B:
    ruisekiwa_of_B.append(ruisekiwa_of_B[-1]+b)
# ansの最大値をとる
ans = 0
for i in range(N+1):
    tmp = 0
    if K >= ruisekiwa_of_A[i]:
        tmp = i
    else:
        continue
    tmp += bisect_right(ruisekiwa_of_B, K-ruisekiwa_of_A[i])-1
    ans = max(ans, tmp)
print(ans)
