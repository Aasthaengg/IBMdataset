S = input()
S = S[::-1]

words = ['dreamer', 'eraser', 'dream', 'erase']
for i in range(4):
    K = words[i]
    words[i] = K[::-1]

T = ''
T_next = ''

while True:
    if len(T) + 5 > len(S):
        break
    for i in range(4):
        S_next = S[len(T):len(T + words[i])]
        T_next = words[i]
        flag = False
        #print(S_next)
        #print(T_next)
        #print()
        if S_next == T_next:
            flag = True
            T += T_next
            #print(T)
            #print()
            #input()
            if T == S:
                print('YES')
                exit()
            break
    if flag == False:
        break
    #input()

print('NO')

