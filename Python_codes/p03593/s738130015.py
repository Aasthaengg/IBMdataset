def main():
    import sys
    input = sys.stdin.readline
    from collections import defaultdict
    H, W = map(int, input().split())
    counter = defaultdict(int)
    for _ in range(H):
        for s in input().rstrip():
            counter[s] += 1
    if H % 2 == 0 and W % 2 == 0:
        for cnt in counter.values():
            if cnt % 4 != 0:
                print("No")
                sys.exit()
        print("Yes")
        sys.exit()
    
    if H % 2 == 1 and W % 2 == 1:
        one_cnt = 0
        two_cnt = 0
        for cnt in counter.values():
            if cnt % 4 != 0:
                if cnt % 2 == 0:
                    two_cnt += 1
                else:
                    one_cnt += 1
        if two_cnt <= H // 2 + W // 2 and one_cnt <= 1:
            print("Yes")
        else:
            print("No")
        sys.exit()
    
    if H % 2 == 1 and W % 2 == 0:
        two_cnt = 0
        for cnt in counter.values():
            if cnt % 4 != 0:
                if cnt % 2 == 0:
                    two_cnt += 1
                else:
                    print("No")
                    sys.exit()
        if two_cnt <= W // 2:
            print("Yes")
        else:
            print("No")
        sys.exit() 

    if H % 2 == 0 and W % 2 == 1:
        two_cnt = 0
        for cnt in counter.values():
            if cnt % 4 != 0:
                if cnt % 2 == 0:
                    two_cnt += 1
                else:
                    print("No")
                    sys.exit()
        if two_cnt <= H // 2:
            print("Yes")
        else:
            print("No")
        sys.exit() 

if __name__ == '__main__':
    main()