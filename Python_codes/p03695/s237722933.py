def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()
    
    n = int(input())
    a = list(map(int, input().split()))
    rate = [0]*8
    cnt = 0
    for x in a:
        r = x//400
        if r > 7:
            cnt += 1
        elif not rate[r]:
            rate[r] = 1
    s = sum(rate)
    mins = s
    if cnt > 0:
        mins += 1
        if s > 0:
            mins -=1
    maxs = s+cnt
    print(mins, maxs)        
        
            



if __name__ == '__main__':
    main()