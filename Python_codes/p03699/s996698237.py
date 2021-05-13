from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    s=[int(readline()) for _ in range(n)]

    max_score=sum(s)
    if max_score%10!=0:
        print(max_score)
    else:
        s.sort()
        flag=False
        for i in range(n):
            if s[i]%10!=0:
                max_score-=s[i]
                flag=True
                break
        print(max_score if flag else 0)
        
if __name__=="__main__":
    main()