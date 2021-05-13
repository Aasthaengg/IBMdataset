import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    i = 0
    while i < n:
        while i+1<n and a[i]==a[i+1]:
            i += 1
        if i+1<n and a[i] < a[i+1]:
            while i+1<n and a[i]<=a[i+1]:
                i += 1
        elif i+1<n and a[i] > a[i+1]:
            while i+1<n and a[i]>=a[i+1]:
                i += 1
        ans += 1
        i += 1
    print(ans)
            
if __name__ == '__main__':
    main()