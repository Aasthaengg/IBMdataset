import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    a, b, k = map(int, input().split())
    cnt = 0
    for i in range(min(a,b), 0, -1):
        if a%i==0 and b%i==0:
            cnt += 1
        if cnt == k:
            print(i)
            return
        
if __name__ == '__main__':
    main()