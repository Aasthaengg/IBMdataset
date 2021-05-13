A = input().split()
S, top = [0], 0


def push(x):
    global top, S
    top += 1
    if len(S) < top + 1:
        S.append(x)
    else:
        S[top] = x


def pop(x):
    global top, S
    top -= 2
    if x == "+":
        push(int(S[top + 1]) + int(S[top + 2]))
    elif x == "-":
        push(int(S[top + 1]) - int(S[top + 2]))
    elif x == "*":
        push(int(S[top + 1]) * int(S[top + 2]))


for i in range(len(A)):
    if str(A[i]).isdigit():
        push(int(A[i]))
    else:
        pop(A[i])
print(S[1])

