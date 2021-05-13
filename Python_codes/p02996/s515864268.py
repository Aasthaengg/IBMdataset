n = int(input())
ba = []

for i in range(n):
    a, b = map(int, input().split())
    ba.append([b, a])

ba.sort()

tm = 0
flg = True
for b, a in ba:
    if tm + a <= b:
        tm += a
    else:
        flg = False

print('Yes' if flg else 'No')
