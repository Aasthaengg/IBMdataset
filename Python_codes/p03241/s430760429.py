import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def main():
    n, m = map(int, readline().split())
    div = []
    for i in range(1, int(m**0.5)+1): 
        if m%i == 0:
            div.append(i)
            div.append(m//i)

    ans = 0
    for d in div:
        if m//n >= d:    
            ans = max(ans, d)
    print(ans)
if __name__ == '__main__':
    main()
