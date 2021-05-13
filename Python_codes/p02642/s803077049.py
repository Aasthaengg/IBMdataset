def main():
    import sys
    input = sys.stdin.readline
    from collections import Counter

    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    cnt = [0]*(10**6+1)
    for a in A:
        if cnt[a]==0:
            x = 2*a   
            while x <= 10**6:
                cnt[x] += 1    
                x += a
        cnt[a] += 1
    print(len([1 for a in A if cnt[a]==1]))

if __name__ == '__main__':
    main()
