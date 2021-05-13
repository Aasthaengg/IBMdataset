A = raw_input().split()
B = []
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
operation = {'+':add, '-':sub, '*':mul}
for item in A:
    if item.isdigit():
        B.append(int(item))
    else:
        num2 = B.pop() 
        num1 = B.pop()
        ans = operation[item](num1, num2)
        B.append(ans)
print ans