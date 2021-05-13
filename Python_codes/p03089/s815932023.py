n = int(input())
a = list(map(int, input().split()))

result =[]
while len(a) > 0:
    ok = False
    for i in range(len(a)-1, -1, -1):
        if i+1 == a[i]:
            result.append(a[i])
            a.pop(i)
            ok = True
            break
    if not ok:
        result = [-1]
        break
for i in result[::-1]: print(i)