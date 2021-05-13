S=input()
S_list=list(S)
words=[chr(i) for i in range(97, 97+26)]

if S=='zyxwvutsrqponmlkjihgfedcba':
    print(-1)

else:
    if len(S)<=25:
        for word in words:
            if not word in S:
                S+=word
                break
        print(S)
    else:
        for n in range(1, 26):
            saisho = S_list[-n]
            N_f = words.index(saisho)
            saigo = S_list[-n - 1]
            N_l = words.index(saigo)
            if N_f < N_l:
                continue
            else:
                S_f = S_list[:-n - 1]
                S_l = S_list[-n:]
                S_l_new = sorted(S_l)
                new = []
                for number in S_l_new:
                    if words.index(number) > N_l:
                        new.append(number)
                        break
                S_f += new
                print(''.join(S_f))
                break
