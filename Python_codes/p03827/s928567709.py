def main():
    n = int(input())
    s = input()
    x = 0
    tmp = 0
    for i in range(len(s)):
        if(s[i]=="D"):
            x-=1
        if(s[i]=="I"):
            x+=1
        tmp = max(tmp,x)
    print(tmp)
if __name__ == '__main__':
    main()
