k, n = map(int, input().split())
dst = list(map(int, input().split()))
dst1 = [k - dst[-1] + dst[0]]
for i in range(1, n):
    dst1.append(dst[i] - dst[i - 1])
dst1.remove(max(dst1))
print(sum(dst1))