import sys

readline = sys.stdin.readline

def main():
    sx, sy, tx, ty = map(int, input().split())
    first = 'R'*(tx-sx) + 'U'*(ty-sy)
    second = 'L'*(tx-sx) + 'D'*(ty-sy)
    third = 'D' + 'R'*(tx-sx+1) + 'U'*(ty-sy+1) + 'L'
    forth = 'U' + 'L'*(tx-sx+1) + 'D'*(ty-sy+1) + 'R'
    ans = first + second + third + forth
    print(ans)

if __name__ == "__main__":
    main()
