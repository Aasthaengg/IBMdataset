from collections import deque
import sys

stack = deque()

def linked_list(stack,command,x=None):

    if command == "insert":#stackの左端にxを追加
        stack.appendleft(x)

    elif command == "delete":#左端から数えて最初のxを削除
        try:
            stack.remove(x)
        except:
            pass

    elif command == "deleteFirst":#左端の要素を削除
        stack.popleft()

    elif command == "deleteLast":#右端の要素を削除
        stack.pop() 


N = int(input())
#lst = [l.split() for l in sys.stdin.readlines()]
#print(lst)
for i in range(N):

    #print(i)
    input_command = input()


    if input_command == "deleteFirst":#左端の要素を削除
        stack.popleft()

    elif input_command == "deleteLast":#右端の要素を削除
        stack.pop() 

    else:
        command,x = input_command.split()
        if command == "insert":#stackの左端にxを追加
            stack.appendleft(x)

        elif command == "delete":#左端から数えて最初のxを削除
            try:
                stack.remove(x)
            except:
                pass

print(" ".join(map(str,stack)))
