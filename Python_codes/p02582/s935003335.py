S = input()

if S == 'RSS':
    print(1)
    exit()

tmp = 0
for i in range(len(S)):
    if S[i] == 'R':
        tmp += 1
    else:
        if i == 2:
            break
        else:
            tmp = 0
print(tmp)            
