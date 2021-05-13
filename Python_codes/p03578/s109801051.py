import collections

def main():
    N = int(input())
    D = list(map(int, input().split()))
    M = int(input())
    T = list(map(int, input().split()))
    Dcounter = collections.Counter(D)
    Tcounter = collections.Counter(T)
    for t in T:
        if Dcounter[t] - Tcounter[t] < 0:
            print('NO')
            return
    print('YES')

if __name__ == "__main__":
    main()
