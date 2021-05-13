from sys import stdin
import string

alpha = string.ascii_lowercase
nokori = [26-i for i in range(26)];nokori[0] = 0
s = stdin.readline().rstrip()
k = int(stdin.readline().rstrip())
sin = ""
for i in s:
    if nokori[alpha.index(i)] <= k:
        k -= nokori[alpha.index(i)]
        sin += "a"
    else:
        sin += i
q = alpha.index(sin[-1])
q += k
print(sin[:-1]+alpha[q%26])