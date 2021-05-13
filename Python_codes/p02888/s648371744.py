n = int(input())
l = sorted(map(int, input().split()))
ret = 0
for i in range(n):
    k = i + 2
    for j in range(i + 1, n):
        while k < n and l[i] + l[j] > l[k]:
            k += 1
        ret += k - j - 1
print(ret)
