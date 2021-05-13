n = int(input())
c = {}
for i in range(n):
    s = input()
    if s in c:
        c[s] += 1
    else:
        c[s] = 1
max = 0
for k in c.keys():
    if c[k] > max:
        max = c[k]
hit = [k for k in c.keys() if c[k] == max]
hit.sort()
for i in range(len(hit)):
    print(hit[i])