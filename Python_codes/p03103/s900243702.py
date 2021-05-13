

n,m = map(int,input().split(" "))
li = []

for i in range(n):
    a,b = map(int,input().split(" "))
    li.append((a,b))

li.sort()

result = 0
count = 0
flag = False
for i in range(m):
    for j in range(li[i][1]):
        result += li[i][0]
        count += 1
        if count == m:
            flag = True
            break
    if flag:
        break
print(result)