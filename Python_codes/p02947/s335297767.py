n = int(input())
s = [input() for _ in range(n)]   
import math

base = []
for i in s:
    base.append(''.join(sorted(i)))
    
base_dict = {}
for i in base:
    if i not in base_dict:
        base_dict[i] = 1
    else:
        base_dict[i] += 1

ans = 0
for key, value in base_dict.items():
    temp = 0
    if value != 1:
        temp = math.factorial(value) // (math.factorial(2) * math.factorial(value-2))
    ans += temp
    
print(ans)