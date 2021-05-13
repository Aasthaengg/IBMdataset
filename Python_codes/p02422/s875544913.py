string = input()
q = int(input())
for c in range(0,q):
    instruction = input().split(' ')
    if instruction[0] == 'print':
        print(string[int(instruction[1]):int(instruction[2]) + 1])
    elif instruction[0] == 'reverse':
        string = string.replace(string[int(instruction[1]):int(instruction[2])+1], string[int(instruction[1]):int(instruction[2])+1][::-1], 1)
    elif instruction[0] == 'replace':
        string = string[:int(instruction[1])] + instruction[3] + string[int(instruction[2])+1:]