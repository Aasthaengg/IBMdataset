from sys import stdin
def main():
    readline=stdin.readline
    s=readline().strip()

    res=0
    for i in range(len(s)):
        if i%2==0:
            if s[i]=="g":
                pass
            else:
                res-=1
        else:
            if s[i]=="g":
                res+=1
            else:
                pass
            
    print(res)

if __name__=="__main__":
    main()