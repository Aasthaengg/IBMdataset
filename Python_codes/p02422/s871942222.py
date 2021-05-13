def my_print():
    print("{}".format("".join(str[command[1]: command[2]])))

def replace():
    command[3] = list(command[3])
    str[command[1]: command[2]] = command[3]

def reverse():
    str[command[1]: command[2]] = reversed(str[command[1]: command[2]])

str = list(input())
q = int(input())
for i in range(q):
    command = input().split()
    command[1], command[2] = int(command[1]), int(command[2]) + 1
    if command[0] == "print":
        my_print()
    elif command[0] == "replace":
        replace()
    else:
        reverse()

