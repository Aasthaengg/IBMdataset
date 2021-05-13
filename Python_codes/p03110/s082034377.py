import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    xu = [list(input().split()) for _ in range(n)]
    ans = 0
    for i in range(n):
        if xu[i][1] == "JPY":
            ans += int(xu[i][0])
        else:
            ans += (float(xu[i][0]) * 380000)
    print(ans)
        
if __name__ == '__main__':
    main()