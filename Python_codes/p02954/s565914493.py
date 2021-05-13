import sys
def S(): return sys.stdin.readline().rstrip()

def Main():
    s = S()
    n = len(s)
    times = 10**100
    ans = [0]*n
    i = 0
    while i<n:
        if s[i]=='L':
            i += 1
            continue
        save = [i]
        while s[i+1]!='L':
            i += 1
            save.append(i)
        flg = save.pop()
        ans[flg] += 1
        for j in range(len(save)):
            tmp = save.pop()
            ans[flg+abs(flg-tmp)%2] += 1
        i += 1
    
    i = n-1
    while 0<=i:
        if s[i]=='R':
            i -= 1
            continue
        save = [i]
        while s[i-1]!='R':
            i -= 1
            save.append(i)
        flg = save.pop()
        ans[flg] += 1
        for j in range(len(save)):
            tmp = save.pop()
            ans[flg-abs(flg-tmp)%2] += 1
        i -= 1
    print(*ans)
    return

if __name__=='__main__':
    Main()