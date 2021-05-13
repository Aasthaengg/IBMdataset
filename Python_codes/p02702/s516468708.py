from collections import defaultdict
S = input()
l = len(S)
d = {0:0}
mod10n = 1
for i in range(1, len(S)+1):
    s = int(S[l-i])
    d[i] = (d[i-1] + s * mod10n) %2019
    mod10n = (mod10n * 10) % 2019
count_d = defaultdict(int)
for key in d.keys():
    count_d[d[key]] += 1
counter = 0
for key in count_d.keys():
    counter += (count_d[key] * (count_d[key]-1)) //2

print(counter)
