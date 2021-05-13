import sys
def input(): return sys.stdin.readline().strip()

def main():
    s = input()
    l = str(len(s) - 2)
    print(s[0] + l + s[-1])
    

if __name__ == "__main__":
    main()
