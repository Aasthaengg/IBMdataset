from bisect import bisect_right
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ruisekiwa_of_a = [0]
ruisekiwa_of_b = [0]
for a in A:
    ruisekiwa_of_a.append(ruisekiwa_of_a[-1]+a)
for b in B:
    ruisekiwa_of_b.append(ruisekiwa_of_b[-1]+b)
# print(ruisekiwa_of_a)
# print(ruisekiwa_of_b)
ans = 0
for i in range(N+1):
    if ruisekiwa_of_a[i] > K:
        continue
    tmp = i
    tmp += bisect_right(ruisekiwa_of_b, K-ruisekiwa_of_a[i])-1
    ans = max(ans, tmp)
print(ans)
