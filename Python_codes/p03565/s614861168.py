S_dash  =   list(input())
len_s   =   len(S_dash)
T       =   list(input())
len_t   =   len(T)

if len_s < len_t:
    print('UNRESTORABLE')
else:
    flag_i = 0
    # if flag_i = 1, it means restorable. if not, unrestorable
    for i in range( len_s - len_t + 1 ):
        flag_j = 0
        # if flag_j = 1 , it means unrestorable
        check_s = S_dash[ len_s - len_t - i : len_s - i ]
        for j in range( len_t ):
            if ( check_s[j] != '?' and check_s[j] != T[j] ):
                flag_j = 1
                break
        if flag_j == 0:
            flag_i = 1
            break
    if flag_i == 0:
        print('UNRESTORABLE')
    else:
        S_dash[ len_s - len_t - i : len_s - i ] = T
        for i in range( len_s ):
            if S_dash[i] == '?':
                S_dash[i] = 'a'
        print( ''.join(S_dash) )