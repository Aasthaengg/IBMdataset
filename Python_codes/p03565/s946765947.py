

def main():
        
    S_part = list(input())
    T_hint = list(input())

    N = len(S_part)
    ans = []

    for i in range(N):
        index_init = i
        
        if (index_init + len(T_hint) <= N):
            s = S_part[index_init:index_init + len(T_hint)]

            if (s == T_hint):
                ans_right = ''.join(S_part[:index_init]).replace('?', 'a')
                ans_middle = ''.join(s)
                tmp_ans = ans_right + ans_middle
                
                if (index_init + len(T_hint) < N):
                    ans_left = ''.join(S_part[index_init + len(T_hint):]).replace('?', 'a')
                    tmp_ans += ans_left
                
                ans.append(tmp_ans)
            

            elif ('?' in s):
                FLAG = True
                
                for j in range(len(s)):
                    if (T_hint[j] != s[j] and s[j] == '?'):
                        s[j] = T_hint[j]
                    
                    elif (T_hint[j] != s[j] and s[j] != '?'):
                        FLAG = False
                        break
                
                
                if (FLAG):
                    ans_left = ''.join(S_part[:index_init])
                    ans_right = ''.join(s)
                    
                    tmp_ans = ans_left + ans_right
                    tmp_ans = tmp_ans.replace('?', 'a')

                    if (index_init + len(T_hint) < N):
                        module = S_part[index_init + len(T_hint):]
                        module = ''.join(module)
                        module = module.replace('?', 'a')
                        
                        tmp_ans += module


                    ans.append(tmp_ans)

    ans.sort()

    if (S_part.count('?') == 0 and T_hint in S_part):
        print(''.join(S_part))
    
    elif (len(ans) > 0):
        print(ans[0])
    
    else:
        print('UNRESTORABLE')


if __name__ == '__main__':
    main()
