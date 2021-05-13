import sys

input = sys.stdin.readline

def main():
    ans = 'NO'
    k = 'keyence'
    S = input().rstrip('\n')
    if S[:7] == k or S[-7:] == k:
        ans = 'YES'
    elif S[0] == k[0]:
        for i in range(1,len(k)):
            if S[i] != k[i]:
                if S[-(7-i):] == k[i:]:
                    ans = 'YES'
                    break
                else:
                  break
    print(ans)

if __name__ == '__main__':
    main()