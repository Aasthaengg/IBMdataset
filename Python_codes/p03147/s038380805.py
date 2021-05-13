import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    h_list = list(map(int, input().split()))
    l = -1
    r = -1
    result = 0
    while any((h > 0 for h in h_list)):
        for i,height in enumerate(h_list):
            if height > 0:
                if l == -1:
                    l = i
                if i == n-1:
                    r = i
                    break
            else:
                if l == -1:
                    continue
                elif r == -1:
                    r = i - 1
                    break

        if l == 0 and r == 0:
             h_list[0] = h_list[0] - 1
        else:
            for i in range(l,r+1):
                h_list[i] = h_list[i] - 1 
        l = -1
        r = -1
        result += 1
    print(result)
    return


if __name__ == '__main__':
    main()