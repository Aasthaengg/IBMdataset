import sys


def input():
    return sys.stdin.readline().strip()

def main():
    a = int(input())
    s = input()
    if a >= 3200:
        print(s)
        return
    print("red")
    
    
main()
