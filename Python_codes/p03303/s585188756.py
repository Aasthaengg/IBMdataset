s = input()
w = int(input())

v = [s[i:i+w] for i in range(0, len(s), w)]

for x in v:
    print(x[0], end='')
print('\n')    
