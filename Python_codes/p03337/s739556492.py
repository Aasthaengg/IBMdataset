A, B = map(int, input().split())

add = A + B
sub = A - B
mul = A * B

if add > sub and add > mul:
    print(add)
elif sub > add and sub > mul:
    print(sub)
elif mul > add and mul > sub:
    print(mul)
else:
    print(add)
