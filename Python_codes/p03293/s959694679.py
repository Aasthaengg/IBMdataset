import numpy as np

def main():
    s = input()
    t = input()
    #n,m = map(int, input().split())
    #a = list(map(int,input().split()))
    l = len(s)
    bool = False
    for i in range(l):
        s = s[l-1]+s[:l-1]
        if s == t:
            bool = True
            break
    if bool == True:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
