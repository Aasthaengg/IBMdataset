A = list(map(str,input().split()))
Stack = []
for e in A:
    if e.isdigit():
        Stack.append(int(e))
    else:
        right = Stack.pop()
        left = Stack.pop()
        if e == "+":
            Stack.append(left+right)
        elif e == "-":
            Stack.append(left-right)
        elif e == "*":
            Stack.append(left*right)
        else:
            if right != 0:
                Stack.append(left//right)
            else:
                print("0?????????")
                exit()

print(Stack.pop())