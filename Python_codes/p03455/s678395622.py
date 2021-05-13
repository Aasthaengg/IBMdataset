def product(a, b):
    return a * b

def judge(num):
    if num % 2 == 0:
        print('Even')
    else:
        print('Odd')

a, b = map(int, input().split())

judge(product(a, b))