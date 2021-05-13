def ABC_101_A():
    S = input()
    sum = 0
    
    for i in range(len(S)):
        if S[i] == '+':
            sum+=1
        else:
            sum-=1

    print(sum)


if __name__ == '__main__':

    ABC_101_A()