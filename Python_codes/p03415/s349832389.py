Strings = [input() for i in range(3)]

output = ''
for n, s in enumerate(Strings):
    output += s[n]
    
print(output)