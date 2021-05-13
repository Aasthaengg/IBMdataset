import sys
input=sys.stdin.readline

def main():
    s = input().strip()
    ans = 0
    x = 0 # g を出した数 - p を出した数
    for c in s:
        if x > 0: # p を出せるので出す
            x -= 1
            if c == "g":
                ans += 1
        else: # g を出す
            x += 1
            if c == "p":
                ans -= 1

    print(ans)

if __name__ == '__main__':
    main()
