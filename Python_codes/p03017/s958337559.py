n,a,b,c,d=map(int,input().split())
s=input()

s="#"+s+"#"

def solve():
    can_reach=True

    for i in range(a,c+1):
        if s[i]=="#" and s[i+1]=="#":
            can_reach=False
            break
    
    for i in range(b,d+1):
        if s[i]=="#" and s[i+1]=="#":
            can_reach=False
            break

    if not can_reach:
        print("No")
        return

    if c>d:
        snuke_can_over=False
        for i in range(b,d+1):
            if s[i-1]=="." and s[i]=="." and s[i+1]==".":
                snuke_can_over=True
                break
        
        if not snuke_can_over:
            print("No")
            return
    
    print("Yes")


if __name__ == "__main__":
    solve()