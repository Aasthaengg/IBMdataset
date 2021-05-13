line = input()
n = int(input())

for _ in range(n):
    command = input().split()
    a = int(command[1])
    b = int(command[2])
    if command[0] == 'print':
        print(line[a:b+1])
    if command[0] == 'reverse':
        line = line[:a] + line[a:b+1][::-1] + line[b+1:]
    if command[0] == 'replace':
        line = line[:a] + command[3] + line[b+1:]
