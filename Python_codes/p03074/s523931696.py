n, k = map(int, input().split())
s = input()
seq = []
pre = '1'
count = 0
for c in s:
    if c == pre:
        count += 1
    else:
        pre = c
        seq.append(count)
        count = 1
seq.append(count)

n = len(seq)
sum = sum(seq[:2*k + 1])
ans = sum
seq.append(0)
for i in range(0, n - 2*k - 1, 2):
    sum -= seq[i] + seq[i + 1]
    sum += seq[i + 2*k + 1] + seq[i + 2 * k + 2]
    ans = max(ans, sum)
print(ans)