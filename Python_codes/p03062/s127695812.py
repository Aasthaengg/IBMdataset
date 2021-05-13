N = int(input())
a = list(map(int,input().split()))
minus = 0
for i in a:
    if i < 0:
        minus += 1
    if i == 0:
        minus = 0
        break
b = []
for j in a:
    b.append(abs(j))
b.sort()
if minus % 2 == 0:
    print(sum(b))
else:
    print(sum(b)-b[0]*2)