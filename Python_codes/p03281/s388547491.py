import sys
read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def divisors(n):
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

def main():
    N = int(readline())
    ans = 0
    for i in range(1,N+1,2):
        div = divisors(i)
        if len(div)==8:
            ans += 1

    print(ans)




if __name__ == '__main__':
    main()
