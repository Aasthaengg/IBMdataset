X = input()

stack_s = []
out = []

for x in X:
    if x == "S":
        stack_s.append("S")
    else:
        if len(stack_s) > 0:
            stack_s.pop()
        else:
            out.append("T")

while len(stack_s) > 0:
    out.append(stack_s.pop())

print(len(out))

