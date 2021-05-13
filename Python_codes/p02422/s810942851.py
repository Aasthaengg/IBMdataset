s = input()
q = int(input())

for i in range(q):
    instruction = list(input().split())
    i_name = instruction[0]
    a, b = int(instruction[1]), int(instruction[2])

    if i_name == 'print':
        print(s[a:b+1])
    elif i_name == 'reverse':
        s = s[:a] + ''.join(list(reversed(s[a:b+1]))) + s[b+1:]
    elif i_name == 'replace':
        p = instruction[3]
        s = s[:a] + p + s[b+1:]

