import sys

def input():
    return sys.stdin.readline().strip()

def main():
    N = int(input())

    def num_divisors_table(n):
        table = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(i, n + 1, i):
                table[j] += 1
        
        return table

    print(sum(num_divisors_table(N-1)))

if __name__ == "__main__":
    main()