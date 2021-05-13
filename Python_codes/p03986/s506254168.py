x = input()
n = len(x)

stack=[]
ans = 1
for i in range(n):
    if(len(stack) > 0 and x[i] == 'T' and stack[-1] == 'S'):
        ans += 1
        stack.pop()
    else:
        stack.append(x[i])
    
print(len(stack))
