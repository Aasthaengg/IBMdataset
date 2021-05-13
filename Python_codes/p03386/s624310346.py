a, b, k = map(int, input().split())

ans_A = []
ans_B = []
for i in range(a, min(b, a + k)):
    ans_A.append(i)
for i in range(max(a, b - k + 1), b+1):
    ans_B.append(i)
ans = sorted(list(set(ans_A) | set(ans_B)))

for i in ans:
    print(i)