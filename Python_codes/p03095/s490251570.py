mod = 10 ** 9 + 7

n = int(input())
s = input()
a = ord('a')

counter = {chr(a + i): 0 for i in range(26)}

for c in s:
  counter[c] += 1
  
result = 1
for v in counter.values():
  result = result * (v + 1) % mod
print(result - 1)