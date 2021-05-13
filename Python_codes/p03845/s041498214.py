import sys
def input(): return sys.stdin.readline().strip()

def main():
    N = int(input())
    T = list(map(int, input().split()))
    M = int(input())
    drink = []
    for _ in range(M):
        p, x = map(int, input().split())
        drink.append((p, x))

    sum_time = sum(T)
    for i in range(M):
        p, x = drink[i]
        p -= 1
        print(sum_time - (T[p] - x))



if __name__ == "__main__":
    main()
