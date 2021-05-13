o = list(str(input()))
e = list(str(input()))

o.reverse()
e.reverse()

n = len(o)+len(e)

ans = []
for i in range(n):
    if i%2 == 0:
        ans.append(o.pop())
    else:
        ans.append(e.pop())
print(''.join(ans))
