import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    a = list(map(int,input().split()))
    ans = []
    for i in range(N):
        l = len(a)
        for i in reversed(range(l)):
            if a[i] == i+1:
                p = a.pop(i)
                ans.append(p)
                break
                
    if a != []:
        print(-1)
    else:
        for i in range(N):
            print(ans[-1-i])

if __name__ == "__main__":
    main()
