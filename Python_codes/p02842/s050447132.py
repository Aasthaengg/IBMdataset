def readinput():
    n=int(input())
    return n

def main(n):
    x7=int(n/1.07)
    x8=int(n/1.08)
    x9=int(n/1.09)
    n100=n*100
    for x in range(max(1,x9-1),x7+1+1):
        xx=x*108//100
        #print(x,xx)
        if xx==n:
            print(x)
            break
    else:
        print(':(')

        

if __name__=='__main__':
    n=readinput()
    main(n)
