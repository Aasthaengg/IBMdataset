import sys
input = sys.stdin.readline

def main():
    x,y,z,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    #a.sort()
    #a.reverse()
    #b.sort()
    #b.reverse()
    #c.sort()
    #c.reverse()
    ans = []
    for i in a:
        for j in b:
            ans.append(i+j)
    ans.sort()
    ans.reverse()
    ans = ans[:k]
    res = []
    for i in c:
        for j in ans:
            res.append(i+j)
    res.sort()
    res.reverse()
    res = res[:k]
    print(*res, sep="\n")
    
if __name__=="__main__":
    main()