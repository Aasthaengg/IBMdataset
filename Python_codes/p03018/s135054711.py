# map(int, input().split())
# list(map(int, input().split()))
# for _ in range(int(input())):
# print(' '.join([str(x) for x in ans]))

s = input()

numBC = 0
total = 0
i = len(s)-1
while i >= 0:    
    if s[i] == 'A':
        total += numBC
    elif s[i] == 'C' and i > 0 and s[i-1] == 'B':
            numBC += 1
            i -= 1
    else:
        numBC = 0
    i-=1

print(total)

