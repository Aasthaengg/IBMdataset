# C - Cat Snuke and a Voyage
def main():
    n, m = map(int, input().split())
    li = [0]*200001

    for _ in range(m):
        a, b = map(int, input().split())
        if a == 1:
            if li[b] == 0:
                li[b] = 1
            else:
                print('POSSIBLE')
                exit()
        if b == n:
            if li[a] == 0:
                li[a] = 1
            else:
                print('POSSIBLE')
                exit()
    else:
        print('IMPOSSIBLE')

if __name__ ==  "__main__":
    main()