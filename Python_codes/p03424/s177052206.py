def ABC_89_B():
    N=int(input())
    s = input().split()
    l = ['P','W','G','Y']
    c=0
    for i in range(len(l)):
        if s.count(l[i])>=1:
            c+=1

    if c==3:
        print('Three')
    else:
        print('Four')

if __name__ == '__main__':

    ABC_89_B()