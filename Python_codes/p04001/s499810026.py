__DEUBG__ = 0
num = input()
pattern = len(num) -1

if pattern == 0:
    print(num)
    exit(0)
total = 0
fmt = '0' + str(pattern) + 'd'
if __DEUBG__:
    print(fmt)
total = 0
for i in range(2**pattern):
    binary = format(int(bin(i)[2:]), fmt)
    if __DEUBG__:
        print('binary', binary)

    equation = ''
    for idx, sign in enumerate(binary):
        equation += num[idx] + ('+' if sign == '1' else '')
        if __DEUBG__:
            print(equation)

    equation += num[-1]
    if __DEUBG__:
        print(equation, eval(equation))
        print()
    total += eval(equation)

print(total)