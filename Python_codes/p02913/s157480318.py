# suffix array
# z-algorithm
# rolling-hash
# dp
n = int(input())
s = input()

# z-algorithm
# i左端
# j iからの距離
# k i-i+jの間を進みながら比較
ans = 0
for num in range(n - 1):
    S = s[num:]
    A = [0] * (n - num)
    A[0] = n - num
    i = 1
    j = 0
    while i < n - num:
        while i + j < n - num and S[j] == S[i + j]:
            j += 1
        A[i] = j
        ans = max(ans, min(i, j))
        if j == 0:
            i += 1
            continue
        k = 1
        while i + k < n - num and k + A[k] < j:
            A[i + k] = A[k]
            ans = max(ans, min(k, A[k]))
            k += 1
        i += k
        j -= k
print(ans)
