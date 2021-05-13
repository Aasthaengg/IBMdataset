a, b = input().split(' ')
a = int(a)
b = int(b)

sum = a+b
mult = a*b
sub = a-b

if sum > mult and sum > sub:
    print(sum)
elif mult > sum and mult > sub:
    print(mult)
else:
    print(sub)

