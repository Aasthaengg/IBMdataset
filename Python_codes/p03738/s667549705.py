import sys
def input(): return sys.stdin.readline().strip()

def main():
    a = int(input())
    b = int(input())
    if a < b:
        print("LESS")
    elif a == b:
        print("EQUAL")
    else:
        print("GREATER")
    

if __name__ == "__main__":
    main()
