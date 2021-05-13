W = input().lower()
wc = 0
while True:
    line = input()
    if line == 'END_OF_TEXT':
        break
        
    for k in line.lower().split():
        if W == k:
            wc += 1

print(wc)