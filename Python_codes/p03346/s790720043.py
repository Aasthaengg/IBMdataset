n = int(input())
p = [0]*n
p2 = []
for i in range(n):
    m = int(input())
    p[m-1] = i
    p2.append(m)

succ = [1] * n

for i in range(1,n):
    if p[i-1] < p[i]:
       succ[i] = succ[i-1] + 1

"""
print(p2)
print(p)
print(succ)
"""

print(n-max(succ))