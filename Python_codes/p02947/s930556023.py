import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N = int(input())
dic_s = {}
for i in range(N):
    s = "".join(sorted(input()))
    if s in dic_s:
        dic_s[s] += 1
    else:
        dic_s[s] = 1
counter = 0
for key,value in dic_s.items():
    if value >1:
        counter += combinations_count(value,2)
print(counter)
