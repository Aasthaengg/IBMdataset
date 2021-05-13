import sys

input = sys.stdin.readline

def main():
    ans = 'NO'
    S = input().rstrip('\n')
    if S.count('KIH') == 1 and S.count('A') <= 4 and S.replace('A', '') == 'KIHBR' and S.count('AA') == 0:
        ans = 'YES'
    print(ans)

if __name__ == '__main__':
    main()