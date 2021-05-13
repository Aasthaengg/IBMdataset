import sys
def input(): return sys.stdin.readline().strip()

def main():
    a, op, b = input().split()
    a = int(a)
    b = int(b)
    if op == '+':
        print(a + b)
    else:
        print(a - b)



if __name__ == "__main__":
    main()
