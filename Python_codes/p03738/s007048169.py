a = input()
b = input()

gt = 'GREATER'
lt = 'LESS'
eq = 'EQUAL'

if len(a) > len(b):
    print(gt)
elif len(a) < len(b):
    print(lt)
elif a == b:
    print(eq)
else:
    for ca, cb in zip(a, b):
        if ca == cb:
            continue
        if ca > cb:
            print(gt)
        else:
            print(lt)
        exit(0)
