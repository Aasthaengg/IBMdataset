n = int(input())

di = len(str(n))
ans = sum([int(w)for w in str(n)])

for i in range(di):
    digits = [int(w)for w in str(n)]
    if digits[i] == 0:
        continue
    t = sum(digits[0:i])

    t += digits[i]-1
    t += 9 * (di - i - 1)
    ans = max(ans, t)

print(ans)
