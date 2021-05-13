Str = input()
q = int(input())
for loop in range(q):
    command = list(map(str,input().split()))
    a = int(command[1])
    b = int(command[2])
    if command[0]=="print":print(Str[a:b+1])
    elif command[0]=="reverse":Str = Str[:a]+Str[a:b+1][::-1]+Str[b+1:]
    else:Str = Str[:a]+command[3]+Str[b+1:]
