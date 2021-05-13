import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    x,y = map(int, readline().split())

    ans = 0

    d = {}
    d[1] = 300000
    d[2] = 200000
    d[3] = 100000

    if x in d:
        ans += d[x]
    
    if y in d:
        ans += d[y]

    if x == 1 and y == 1:
        ans += 400000
    
    print(ans)
    

if __name__ == "__main__":
    main()
