import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    m,p = [],[]
    
    for x,y in zip(a,b):
        if x > y:
            p.append(x-y)
        elif x < y:
            m.append(y-x)

    ch = sum(m)
    p.sort(reverse=True)
    ans = len(m)
    l = 0
    while ch > 0:
        if l == len(p):
            print(-1)
            exit()
        else:
            ch -= p[l]
            ans += 1
            l += 1
            
    print(ans)

if __name__ == "__main__":
    main()
