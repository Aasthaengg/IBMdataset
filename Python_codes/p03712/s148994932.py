# 2020/06/10
# AtCoder Beginner Contest 062 - B

# Input
h, w = map(int,input().split())
header = ['#'] * (w+2)
print(''.join(header))

# Calc
for i in range(h):
    instr = input()
    wstr = '#' + instr + '#'
    print(wstr)

print(''.join(header))
