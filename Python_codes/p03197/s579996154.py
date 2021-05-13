n = int(input())
a = []
ans = 'second'
for i in range(n):
    ai = int(input())
    a.append(ai)
    if ai % 2 == 1:
        ans = 'first'
print(ans)