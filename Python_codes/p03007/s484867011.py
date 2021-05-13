n = int(input())
A = list(map(int, input().split()))
A.sort()
amin = A[0]
amax = A[-1]
B = A[1:-1]
action = []
for b in B:
    if b < 0:
        action.append((amax, b))
        amax -= b
    else:
        action.append((amin, b))
        amin -= b
action.append((amax, amin))
score = amax - amin
print(score)
for x, y in action:
    print('{} {}'.format(x, y))