#-*-coding:utf-8-*-

def main():
    a,b,c = map(int,input().split())
    ans=b//a
    if c > ans:
        print(ans)
    else:
        print(c)

if __name__=="__main__":
    main()