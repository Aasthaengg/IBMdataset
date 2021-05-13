import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    ans = 0
    cumsum = [0] * (n + 1)
    for i in range(len(l)):
        cumsum[i+1] = cumsum[i] + l[i]
    for i in cumsum:
        if i <= x:
            ans += 1
        else:
            break
    print(ans)
    
if __name__ == '__main__':
    main()