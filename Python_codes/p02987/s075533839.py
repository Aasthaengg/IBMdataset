def ABC_132_A():
    S = input()
    if S.count(S[0]) != 2 or S.count(S[1]) != 2 or S.count(S[2]) != 2 or S.count(S[3]) != 2:
        print('No')
    else:
        print('Yes')
 
if __name__ == '__main__':
 
    ABC_132_A()