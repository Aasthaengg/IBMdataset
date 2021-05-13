def ABC_139_A():
    S = input()
    T = input()
    atari = 0
    
    for i in range(3):
        if S[i] == T[i]:
            atari+=1
    print(atari)

if __name__ == '__main__':

    ABC_139_A()