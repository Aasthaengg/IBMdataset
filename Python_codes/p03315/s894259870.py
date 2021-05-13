import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    S = readline().strip()

    ans = 0
    for s in S:
        if s == "+":
            ans += 1
        else:
            ans -= 1
    
    print(ans)


if __name__ == "__main__":
    main()
