weather = input()

seq = 0
prev = False
for i in range(3):
    if weather[i] == 'R':
        if prev:
            seq += 1
            prev = True
        else:
            seq = 1
            prev = True
    else:
        prev = False
            
print(seq)