a, b, c, d = [int(c) for c in input()]

done = False
ops = ['+', '-']
for op1 in ops:
    for op2 in ops:
        for op3 in ops:
            left = a
            left += b if op1 == '+' else -b
            left += c if op2 == '+' else -c
            left += d if op3 == '+' else -d
            if left == 7:
                done = True
                break
        if done:
            break
    if done:
        break
print('{a}{op1}{b}{op2}{c}{op3}{d}=7'.format(a=a, b=b, c=c, d=d, op1=op1, op2=op2, op3=op3))
