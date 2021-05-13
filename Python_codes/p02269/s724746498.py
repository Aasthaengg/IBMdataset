n = int(input())

s = set()

for _ in range(n):
    instruction, word = input().split()
    if instruction == 'insert':
        s.add(word)
    else:
        if word in s:
            print('yes')
        else:
            print('no')
