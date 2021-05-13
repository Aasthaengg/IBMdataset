from collections import deque

def solve():
    n,a,b,c,d = map(int,input().split())
    s = input()
    # aからcに到達可能か
    flag1 = True
    # bからcに到達可能か
    flag2 = True
    # 反転しているとき、到達可能な範囲に...は存在するか
    flag3 = False
    cnt = 0
    for i in range(a-1,c):
        if s[i]=='#':
            cnt+=1
        else:
            cnt=0
        if cnt>=2:
            flag1 = False
    cnt=0
    for i in range(b-1,d):
        if s[i]=='#':
            cnt+=1
        else:
            cnt=0
        if cnt>=2:
            flag2 = False
    l = max(a,b)
    r = min(c,d)
    if r<n and s[r]!='#':
        r+=1
    if l-2>=0 and s[l-2]!='#':
        l-=1
    for i in range(l-1,r):
        if s[i]=='.':
            cnt+=1
        else:
            cnt=0
        if cnt>=3:
            flag3 = True

    if flag1 and flag2:
        if c<d:
            print('Yes')
        else:
            if flag3:
                print('Yes')
            else:
                print('No')
    else:
        print('No')
        
if __name__ == "__main__":
    solve()