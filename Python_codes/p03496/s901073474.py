N = int(input())
a = list(map(int, input().split()))

op = []
maxa = -10**7
argmaxa = -1
for i in range(N):
    if a[i] > maxa:
        maxa = a[i]
        argmaxa = i

mina = 10**7
argmina = -1
for i in range(N):
    if a[i] < mina:
        mina = a[i]
        argmina = i

if mina >= 0:
    pass
elif maxa <= 0:
    pass
elif abs(maxa) > abs(mina):
    for i in range(N):
        a[i] += maxa
        op.append((argmaxa, i))
else:
    for i in range(N):
        a[i] += mina
        op.append((argmina, i))
if abs(maxa) > abs(mina):
    for i in range(N-1):
        a[i+1] += a[i]
        op.append((i, i+1))
else:
    for i in reversed(range(1, N)):
        a[i-1] += a[i]
        op.append((i, i-1))

print(len(op))
for elem in op:
    print(' '.join(map(lambda x: str(x+1), elem)))
