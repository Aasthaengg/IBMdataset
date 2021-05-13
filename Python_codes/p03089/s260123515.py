n = int(input())
b = list(map(int, input().split()))

a = []
flg = True
while b:
    for i in range(len(b), 0, -1):
        if b[i-1] == i:
            a.append(b.pop(i-1))
            break
        elif i == 1:
            flg = False
            break
    if not flg:
        break
a.reverse()
a = [str(i) for i in a]
print('\n'.join(a)) if flg else print(-1)