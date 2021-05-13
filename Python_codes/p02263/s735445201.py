S = raw_input().split(" ")
Stack = list()

def push(x):
    Stack.append(x)

def pop():
    return Stack.pop(-1)

a = 0
b = 0
for i in range(len(S)):
    if S[i] == "+":
        a = pop()
        b = pop()
        push(b + a)
    elif S[i] == "-":
        a = pop()
        b = pop()
        push(b - a)
    elif S[i] == "*":
        a = pop()
        b = pop()
        push(b * a)
    elif S[i] == "/":
        a = pop()
        b = pop()
        push(b / a)
    else:
        push(int(S[i]))

print Stack.pop(-1)