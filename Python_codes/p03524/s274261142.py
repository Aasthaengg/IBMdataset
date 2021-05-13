import sys
#input = sys.stdin.buffer.readline
from collections import Counter

def main():
    s = list(input())
    l = len(s)
    c = Counter(s)
    c = list(c.values())
    
    c.sort(reverse=True)

    for num in c:
        if num != -(-l//3):
            print("NO")
            exit()
        l -= 1

    print("YES")

if __name__ == "__main__":
    main()
