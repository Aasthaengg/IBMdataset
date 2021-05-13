n = int(input())
b = list(map(int,input().split()))
a = []
flag = 0

for i in range(n):
    tmp = []
    for j in range(len(b)):
        if j+1 == b[j]:
            tmp.append(b[j])
    if len(tmp) == 0:
        flag= 1
        break
    a.append(b.pop(tmp[-1]-1))

if flag == 0:
    for i in range(len(a)):
        print(a[-1-i])
else:
    print(-1)
