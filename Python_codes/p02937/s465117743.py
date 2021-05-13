from sys import stdin
import bisect
def main():
    #入力
    readline=stdin.readline
    s=readline().strip()
    n=len(s)
    t=readline().strip()

    d=dict()
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]]=[i]
        else:
            d[s[i]].append(i)
        
    j=-1
    cnt=0
    ans=0
    for i in range(len(t)):
        if t[i] not in d:
            print(-1)
            break
        k=bisect.bisect_right(d[t[i]],j)
        if k<len(d[t[i]]):
            j=d[t[i]][k]
        else:
            cnt+=1
            j=d[t[i]][0]
        ans=j+cnt*n
    else:
        print(ans+1)

if __name__=="__main__":
    main()