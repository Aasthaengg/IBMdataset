string = input()

new = [string[i] for i in range(len(string)) if i % 2 == 0]

print(''.join(new))