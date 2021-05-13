s = input()
num_C = 0

for i in range(len(s)):
    if i == 0:
        if s[i] != 'A':
            print('WA')
            exit() 
    elif i >= 2 and i <= len(s)-2:
        if s[i] == 'C': num_C += 1
    else:
        if ord(s[i]) < ord('a') or ord(s[i]) > ord('z'):
            print('WA')
            exit()
if num_C != 1:
    print('WA')
    exit()
print('AC')