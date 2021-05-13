import copy
n = int(input())
a = [int(input()) for A in range(n)]
max_a,secound_max_a = max(a),0
b = copy.copy(a)
b.sort()
bol = True
for j in range(n,n,-1):
    if b[j] != max(a):
        secound_max_a = b[j]
        bol = False
        break
if bol:
    secound_max_a = b[-2]

for i in range(n):
    if a[i] != max_a:
        print(max_a)
    else:
        print(secound_max_a)