s = input()

r = 0
dict_r = {0: 1}
r10 = 1
for i in range(len(s)):
    d = int(s[-i - 1])
    r = (r + d * r10) % 2019
    r10 = (r10 * 10) % 2019

    dict_r[r] = dict_r.get(r, 0) + 1


answer = sum(v * (v - 1) // 2 for v in dict_r.values())
print(answer)
