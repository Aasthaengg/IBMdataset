def main():
    X = input()
    delcnt = 0
    delans = 0
    for i in range(len(X)):
        if X[i]=='S':
            delcnt += 1
        if X[i]=='T' and delcnt>0:
            delans +=2
            delcnt -=1
    print(len(X)-delans)



if __name__ == '__main__':
    main()