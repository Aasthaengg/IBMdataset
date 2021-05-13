import sys
input = sys.stdin.readline

def main():
    s= input().strip()
    p = s.count("p")
    print((len(s)//2) - p)

if __name__ == "__main__":
    main()