N = int(input())
d = [0]*5
for i in range(N):
    st = input()
    if st[0] == 'M': d[0] += 1
    if st[0] == 'A': d[1] += 1
    if st[0] == 'R': d[2] += 1
    if st[0] == 'C': d[3] += 1
    if st[0] == 'H': d[4] += 1

res = 0

for i in range(3):
    for j in range(i+1,4):
        for k in range(j+1,5):
            res += d[i]*d[j]*d[k]
print(res)
