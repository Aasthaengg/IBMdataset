from sys import stdin
def main():
    #入力
    readline=stdin.readline
    s=readline().strip()
    x,y=map(int,readline().split())
    n=len(s)

    now_x={0}
    now_y={0}
    i=0
    first=True
    flag="x"
    cnt=0
    while i<n:
        if s[i]=="F":
            cnt+=1
            i+=1
            if i==n:
                nex=set()
                if flag=="x":
                    l=len(now_x)
                else:
                    l=len(now_y)
                for _ in range(l):
                    if flag=="x":
                        now=now_x.pop()
                    else:
                        now=now_y.pop()
                    nex.add(now+cnt)
                    if first==False:
                        nex.add(now-cnt)
                if flag=="x":
                    now_x=nex
                    flag="y"
                else:
                    now_y=nex
                    flag="x"
        else:
            nex=set()
            if flag=="x":
                l=len(now_x)
            else:
                l=len(now_y)
            for _ in range(l):
                if flag=="x":
                    now=now_x.pop()
                else:
                    now=now_y.pop()
                nex.add(now+cnt)
                if first==False:
                    nex.add(now-cnt)
            if flag=="x":
                now_x=nex
                flag="y"
            else:
                now_y=nex
                flag="x"
            if first:
                first=False
            i+=1
            cnt=0

    if x in now_x and y in now_y:
        print("Yes")
    else:
        print("No")

if __name__=="__main__":
    main()