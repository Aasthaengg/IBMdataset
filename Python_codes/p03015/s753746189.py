import sys
def input(): return sys.stdin.readline().strip()
mod = 10**9+7

def main():
    L = input()
    l = len(L)
    """
    LについてbitDP、かつa, bは同じ桁に1, 1とならない
    """
    stoic = 2
    affordable = 1
    for i in range(1, l):
        if L[i] == '1':
            affordable = (stoic + affordable * 3) % mod
            stoic = (stoic * 2) % mod
        else:
            affordable = (affordable * 3) % mod

    print((stoic + affordable) % mod)







if __name__ == "__main__":
    main()
