N, K = map(int, input().split())
A = list(map(int, input().split()))
bin_str1 = format(K+1, "b")
bin_str2 = format(max(A), "b")
l = max(len(bin_str1), len(bin_str2))
P = [0]*l

for i in range(N):
    t = format(A[i], "b")
    t = t[::-1]
    for j in range(len(t)):
        if t[j] == "1":
            P[j] += 1

if N % 2 == 0:
    bor = N//2
else:
    bor = N//2 + 1

result = 0
bin_str1 = bin_str1[::-1]
for i in range(len(bin_str1)):
    s = 1
    ans = 0
    if bin_str1[i] == "1":
        for j in range(i):
            if P[j] >= bor:
                ans += s*P[j]
            else:
                ans += s*(N - P[j])
            s *= 2
        ans += s*P[i]
        s *= 2
        for j in range(i+1, len(bin_str1)):
            if bin_str1[j] == "0":
                ans += s*P[j]
            else:
                ans += s*(N - P[j])
            s *= 2
        if len(bin_str2) > len(bin_str1):
            for j in range(len(bin_str1), len(bin_str2)):
                ans += s*P[j]
                s *= 2
    result = max(ans, result)

print(result)