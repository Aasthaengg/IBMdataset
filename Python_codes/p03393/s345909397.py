from sys import stdin
def main():
    #入力
    readline=stdin.readline
    S=readline().strip()
    N=len(S)
    alps=[chr(i) for i in range(97,97+26)]
    flags=[False]*26
    if N<26:
        for i in range(N):
            flags[ord(S[i])-97]=True
        for i in range(26):
            if flags[i]==False:
                s=alps[i]
                break
        print(S+s)

    else:
        if S=="zyxwvutsrqponmlkjihgfedcba":
            print(-1)
        else:
            k=0
            for i in range(26):
                if i==0:
                    j=ord(S[i])-97
                else:
                    if ord(S[i-1])-97<ord(S[i])-97:
                        k=i
                        j=ord(S[i])-97

            target1=S[k-1]
            for i in range(k,26):
                if i==k:
                    target2=S[k]
                else:
                    if ord(target1)-97<ord(S[i])-97<ord(target2)-97:
                        target2=S[i]

            print(S[:k-1]+target2)

if __name__=="__main__":
    main()