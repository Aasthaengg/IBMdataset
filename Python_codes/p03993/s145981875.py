import sys

input = sys.stdin.readline

def main():
    ans = 0
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[a[i]-1] == i+1:
            ans +=1
    print(ans//2)

if __name__ == '__main__':
    main()