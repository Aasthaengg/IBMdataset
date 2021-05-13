import sys

def isPrime(i):
    if i == 2: return True
    k = 2
    while k ** 2 <= i:
        if i % k == 0: return False
        k += 1
    return True
            
def solve():
    input = sys.stdin.readline
    N = int(input())
    count = 0
    k = 1
    Ans = []
    while count < N:
        if isPrime(5 * k + 1):
            Ans.append(5 * k + 1)
            count += 1
        k += 1
    print(" ".join(map(str, Ans)))
    return 0

if __name__ == "__main__":
    solve()