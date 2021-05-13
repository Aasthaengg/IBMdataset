S = input()
mod = [0 for _ in range(len(S))]
mod[0] = int(S[-1])
for i in range(1, len(S)):
    mod[i] = (mod[i - 1] + pow(10, i, 2019) * int(S[-1 - i])) % 2019
ans = 0
res = [0 for _ in range(2019)]
for i in range(len(S)):
    ans += res[mod[i]]
    res[mod[i]] += 1
print(ans + res[0])