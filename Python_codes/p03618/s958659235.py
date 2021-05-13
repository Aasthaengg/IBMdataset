from collections import Counter


A = input()

ret = len(A) * (len(A) - 1) // 2 + 1
for v in Counter(A).values():
  ret -= v * (v - 1) // 2
  
print(ret)