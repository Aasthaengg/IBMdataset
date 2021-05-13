s = input().split()

h = int(s[0])
w = int(s[1])

strings = []

for i in range(h):
    p = input()
    strings.append(p)

for i in range(w + 2):
    print('#', end='')

print('')


for i in range(h):
    print('#', end='')
    print(strings[i], end='')
    print('#')

for i in range(w + 2):
    print('#', end='')
    
print('')
