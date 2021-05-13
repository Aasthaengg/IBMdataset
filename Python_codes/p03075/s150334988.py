def ABC_123_A():

    a = [0 for i in range(6)]

    count=0
   
    for i in range(6):
        a[i] = int(input())

    for i in range(5):
        for j in range(4):
            if i+j+1 <= 4:
                if abs(a[i] - a[i+j+1]) > a[5]:
                    count=1
                else:
                    count+=0
            else:
                count+=0
    if count == 1:
        print(':(')
    else:
        print('Yay!')

if __name__ == '__main__':

    ABC_123_A()