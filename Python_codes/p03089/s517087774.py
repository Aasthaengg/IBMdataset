N = int(input())
b = list(map(int, input().split()))

c = b[:]
ans = []
jdg = True

while c:
    temp = []
    for i in range(len(c)):
        if i + 1 - c[i] == 0:
            temp.append([c[i], i])
    if not temp:
        jdg = False
        break
    l = max(temp)
    c = c[:l[1]] + c[l[1]+1:]
    ans.append(l[0])

if jdg:
    ans.reverse()
    print(*ans, sep='\n')
else: print(-1)