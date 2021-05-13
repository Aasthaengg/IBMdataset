n = int(input())

data = []
for i in range(n):
    s,p = input().split()
    p = int(p)
    data.append((s,-p,i))

sorted_data = sorted(data, key=lambda x:(x[0], x[1]), reverse=False)

for i in range(n):
    print(sorted_data[i][2] + 1)