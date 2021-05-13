str = input()
q = int(input())

for _ in range(q):
    line = input().split()
    c = line[0]
    a = int(line[1])
    b = int(line[2]) + 1

    if c == 'replace':
        str = str[:a] + line[3] + str[b:]
    elif c == 'reverse':
        str = str[:a] + str[a:b][::-1] + str[b:]
    else:
        print(str[a:b])