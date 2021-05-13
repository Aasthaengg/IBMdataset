text = input()
count = int(input())

for c in range(count):
    args = input().split()
    (a, b) = [int(x) for x in args[1:3]]
    if args[0] == 'print':
        print(text[a:b + 1])
    elif args[0] == 'reverse':
        text = text[0:a] + text[a:b + 1][::-1] + text[b + 1:]
    elif args[0] == 'replace':
        text = text[0:a] + args[3] + text[b + 1:]