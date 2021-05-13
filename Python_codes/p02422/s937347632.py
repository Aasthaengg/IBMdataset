# coding:utf-8
def show(a,b):
    global str
    print str[a:b+1]
def reverse(a,b):
    global str
    t = str[:a]
    t += str[-(len(str)-b):-(len(str)-a+1):-1]
    t += str[b+1:]
    str = t
def replace(a,b,p):
    global str
    t = str[:a]
    t += p
    t += str[b+1:]
    str = t

str = raw_input()
n = input()

for i in range(n):
    command = raw_input().split()
    if command[0] == "replace":
        replace(int(command[1]),int(command[2]),command[3])
    elif command[0] == "reverse":
        reverse(int(command[1]),int(command[2]))
    elif command[0] == "print":
        show(int(command[1]),int(command[2]))


