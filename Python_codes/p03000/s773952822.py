n, x = map(int, input().split())
(*l,) = map(int, input().split())
a = [0]
for i in l:
    if a[-1] + i > x:
        break
    a.append(a[-1] + i)
print(len(a))