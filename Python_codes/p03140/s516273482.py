def main():
    N = int(input())
    A = input()
    B = input()
    C = input()
    ans = 0
    for a,b,c in zip(A,B,C):
        now = set([a,b,c])
        if len(now)==1:
            pass
        elif len(now)==2:
            ans += 1
        else:
            ans += 2
    
    print(ans)
if __name__ == '__main__':
    main()