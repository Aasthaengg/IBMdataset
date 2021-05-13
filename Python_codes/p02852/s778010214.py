N, M = list(map(int, input().split(' ')))
S = input()

# print("%d,%d" % (N, M))
# print(S)
if S[0] == 1 or S[-1] == 1:
    print(-1) # no route
    exit(0)

pos = len(S) - 1
move = []
while pos >= 0:
    if pos - M <= 0:
        move.append(pos)
        break
    
    found = False
    for idx in range(pos - M, pos):
        if S[idx] == '0':
            found = True
            break
    
    if not found:
        move = None
        break # no route
    
    move.append(pos - idx)
    pos = idx

if move is None:
    print(-1)
else:
    move.reverse()
    print(' '.join(list(map(str, move))))
