# -*- coding: utf-8 -*-

numbers = list("1234567890")
querry = [n for n in input().split()]

stack = []

for q in querry:
    if q == "+":
        stack.append(stack.pop() + stack.pop())
    elif q == "-":
        stack.append(-stack.pop() + stack.pop())
    elif q == "*":
        stack.append(stack.pop() * stack.pop())
    else:
        stack.append(int(q))

print(stack.pop())