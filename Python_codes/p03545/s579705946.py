import itertools
a, b, c, d = map(int, list(input()))
l1 = [1, -1]
l2 = [1, -1]
l3 = [1, -1]

for op1, op2, op3 in itertools.product(l1, l2, l3):
    tmp = a + b*op1 + c*op2 + d*op3
    if tmp == 7:
        break

op1, op2, op3 = map(lambda x: "+" if x==1 else "-", [op1, op2, op3])

print(str(a)+op1+str(b)+op2+str(c)+op3+str(d)+"=7")