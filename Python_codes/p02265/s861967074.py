from collections import deque
n = int(input())
output = deque()
for i in range(n):
    li = input().split(' ')
    if(li[0] == 'insert'):
        output.appendleft(li[1])
    elif(li[0] == 'deleteFirst'):
        output.popleft()
    elif(li[0] == 'deleteLast'):
        output.pop()
    elif(li[0] == 'delete'):
        try:
            output.remove(li[1])
        except:
            pass
print(' '.join(output))
