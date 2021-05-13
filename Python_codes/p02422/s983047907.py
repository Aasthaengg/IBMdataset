string = raw_input()
num_order = int(raw_input())
for i in range(num_order):
    command = raw_input().split()
  #  print command
    a, b = map(int, command[1:3])
    if command[0] == "print":
        print string[a:b+1]
    elif command[0] == "reverse":
        string = string[:a] + string[a:b+1][::-1] + string[b+1:]
    elif command[0] == "replace":
        p = command[-1]
        string = string[:a] + p + string[b+1:]