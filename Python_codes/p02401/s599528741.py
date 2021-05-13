import sys

while(True):
    a, op, b = sys.stdin.readline().split()
    if(op == '?'):
        break
    a, b = map(int, [a, b])
    ans = 0
    if(op == '+'):
        ans = a + b
    if(op == '-'):
        ans = a - b
    if(op == '*'):
        ans = a * b
    if(op == '/'):
        ans = int(a / b)
    print(ans)