n = int(input())
d = set() 
result = []
for _ in range(n):
    command, s = input().split()
    if command == 'insert':
        d.add(s)
    elif command == 'find':
        if s in d:
            result.append('yes')
        else:
            result.append('no')

for r in result:
    print(r)

