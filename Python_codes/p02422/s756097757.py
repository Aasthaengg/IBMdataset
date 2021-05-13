str1 = input()
count = int(input())

for i in range(count):
    args = input().split()
    (a,b) = [int(x) for x in args[1:3]]
    if args[0] == 'print':
        print(str1[a:b + 1])
    elif args[0] == 'reverse':
        str1 = str1[0:a] + str1[a:b + 1][::-1] + str1[b + 1:]
    elif args[0] == 'replace':
        str1 = str1[0:a] + args[3] + str1[b + 1:]