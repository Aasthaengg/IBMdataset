s = input().split()
n = int(s[0])
k = int(s[1])

arrays = []
answer = 0
count = 0

for i in range(100001):
    arrays.append(0)

for i in range(n):
    v = input().split()
    p = int(v[0])
    q = int(v[1])
    arrays[p] += q

for i in range(len(arrays)):
    if not arrays[i] == 0:
        count += arrays[i]
        if k <= count:
            answer = i
            break

print(answer)

