text = input()
for i in range(int(input())):
    ls = list(input().split())
    command = (ls[0])
    a = int(ls[1])
    b = int(ls[2])+1
    if command == 'print':
        print(text[a:b])
    elif command == 'reverse':
        text = text[:a] + text[a:b][::-1] + text[b:]
    elif command == 'replace':
        text =  text[:a] + ls[3] + text[b:]