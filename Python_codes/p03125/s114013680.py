import sys
def input(): return sys.stdin.readline().strip()

def main():
    a,b=map(int,input().split())
    if b%a:
        print(b-a)
    else:
        print(a+b)

main()