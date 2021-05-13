import sys
def input(): return sys.stdin.readline().strip()
mod = 10**9+7

def main():
    n = int(input())
    power = 1
    for i in range(1, n + 1):
        power *= i
        power %= mod
    print(power)
    

if __name__ == "__main__":
    main()
