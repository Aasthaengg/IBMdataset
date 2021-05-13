import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    a, b = map(int, input().split())
    r = 0
    for i1 in range(a, b + 1):
        c1 = i1 // 10000 == i1 % 10
        c2 = ((i1 // 1000) % 10) == ((i1//10)%10)
        r += c1 and c2
    print(r)

if __name__ == '__main__':
    main()