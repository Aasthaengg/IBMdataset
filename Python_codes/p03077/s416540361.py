
def solve():
    ABCDEmin = min(ABCDE)
#    print(ABCDEmin)
    if N % ABCDEmin == 0:
        t = N//ABCDEmin + 4
    else:
        t = N//ABCDEmin + 4 + 1
    print(t)

        

if __name__ == "__main__":
    N = int(input())
    ABCDE = [int(input()) for _ in range(5)]
    solve()
