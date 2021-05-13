SA = input()
SB = input()
SC = input()

S_dict={'a':SA,'b':SB,'c':SC}
ans_dict={'a':'A','b':'B','c':'C'}

person = 'a'

while True:
    S = S_dict[person]

    if len(S) <= 0:
        print(ans_dict[person])
        break
        
    else:
        S_dict[person] = S[1:]
        person = S[0]