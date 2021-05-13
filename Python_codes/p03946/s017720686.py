def main():
    import sys 
    input = sys.stdin.readline
    n,t = map(int,input().split())
    l = list(map(int,input().split()))
    ans = []
    check = l[0]
    for i in l:
        if i < check:
            check = i
        else:
            dis = i-check
            ans.append(dis)
    print(ans.count(max(ans)))

if __name__ == "__main__":
    main()

        
