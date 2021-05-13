import sys

def main():
    X=int(input())
    s=0
    i=0
    while s<X:
        i+=1
        s+=i
    print(i)
if __name__=='__main__':
    main()

