import copy

def main():
    N = int(input())
    T = list(map(int, input().split()))
    M = int(input())
    PX = []
    for i in range(M):
        P, X = map(int, input().split())
        tmp = copy.copy(T)
        tmp[P-1] = X
        print(sum(tmp))

if __name__ == "__main__":
    main()
