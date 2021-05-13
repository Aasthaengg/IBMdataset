def main():
    import sys
    from collections import defaultdict
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    D = defaultdict(int)
    H, W = [int(x) for x in input().strip().split()]
    four_pair = (H // 2) * (W // 2)
    two_pair = H % 2 * W // 2 + W % 2 * H // 2
    one = H % 2 * W % 2
    for h in range(H):
        for s in list(input().strip()):
            D[s] += 1
    
    for d, i in D.items():
        while four_pair and i >= 4:
            four_pair -= 1
            i -= 4
        D[d] = i
    if four_pair:
        print('No')
        return False

    for d, i in D.items():
        while two_pair and i >= 2:
            two_pair -= 1
            i -= 2
        D[d] = i
    if two_pair:
        print('No')
        return False
    
    if one == sum(D.values()):
        print('Yes')
        return True
    else:
        print('No')
        return False

if __name__ == '__main__':
    main()