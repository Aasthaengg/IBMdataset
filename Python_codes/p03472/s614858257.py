from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n,h=map(int,readline().split())
    li=[list(map(int,readline().split())) for _ in range(n)]
    li.sort(key=lambda x:x[1])
    a_max=0
    j=-1
    for i in range(n):
        if a_max<li[i][0]:
            a_max=li[i][0]
            j=i
    flags=[True]*n
    is_killed=False
    cnt=0
    for i in range(n-1,-1,-1):
        if i==j:
            if h<=li[i][1]:
                cnt+=1
                is_killed=True
                break
        elif a_max<li[i][1]:
            cnt+=1
            flags[i]=False
            h-=li[i][1]
            if h<=0:
                is_killed=True
                break
        else:
            break

    if is_killed:
        print(cnt)
    else:
        if h<=li[j][1]:
            cnt+=1
        elif li[j][0]>=li[j][1]:
            cnt+=(h+a_max-1)//a_max
        else:
            cnt+=1
            h-=li[j][1]
            cnt+=(h+a_max-1)//a_max
    
        print(cnt)

if __name__=="__main__":
    main()