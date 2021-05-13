A, B, C = map(int, input().split())

not_poison = A+B
poison = C

if poison > not_poison :
    if poison - not_poison != 0:
        print(B + not_poison + 1)
    else:
        print(B + not_poison)
else:
    print(B + poison)