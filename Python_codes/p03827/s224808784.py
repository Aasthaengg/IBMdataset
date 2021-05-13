def ABC_52_B():
    N = int(input())
    S = input()
    xl=[]
    x=0

    for i in range(N):
        if S[i] == 'I':
            x+=1
        else:
            x-=1

        xl.append(x)
    
    if max(xl)>=0:
        print(max(xl))
    else:
        print(0)

if __name__ == '__main__':

    ABC_52_B()