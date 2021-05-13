from sys import stdin
def main():
    #入力
    readline=stdin.readline
    s=readline().strip()

    cnt=1
    for i in range(len(s)):
        if i==0:
            now=s[i]
        else:
            if now!=s[i]:
                cnt+=1
                now=s[i]

    print(cnt-1)

if __name__=="__main__":
    main()