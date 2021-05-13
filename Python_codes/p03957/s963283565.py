s = list(input())
i = 0
while i < len(s):
    if s[i] == 'C':
        j = i + 1
        while j < len(s):
            if s[j] == 'F':
                print('Yes')
                exit(0)
            j = j + 1
    i = i + 1

print('No')