from sys import stdin

input = stdin.readline

def main():
    X = int(input().rstrip())
    ans = 1
    n = X
    while(n % 360 != 0):
        n += X
        ans += 1 
    print(ans)

if __name__ == "__main__":
    main()
    
