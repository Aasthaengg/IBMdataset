ans = [1,2,3]
tmp = []

for i in range(2):
    tmp.append(int(input()))

for j in ans:
    if j not in tmp:
        print(j)
