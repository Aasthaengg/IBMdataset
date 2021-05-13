import math
S = input()
w = int(input())
stack = []
for x in range(math.ceil(len(S)/w)):
    stack.append(S[x*w])
print("".join(stack))
