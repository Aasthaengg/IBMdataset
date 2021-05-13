import sys
input = sys.stdin.readline
def main():
    S = input().rstrip()
    L = len(S)
    if S[0] == 'A':
        CNT = 0
        CAP = 0
        for c in range(2,L-1):
            if S[c] == 'C':
                CNT += 1
        for c in S:
            if ord(c) >= 97:
                CAP += 1
        if CNT == 1 and CAP == L-2:
            print('AC')
        else:
            print('WA')
    else:
        print('WA')

if __name__ == '__main__':
    main()