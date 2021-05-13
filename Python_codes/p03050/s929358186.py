import sys
input = sys.stdin.readline

def main():
    n = int(input())

    def yakusu():
        for i in range(1, int(n**0.5)+1):
            if n%i == 0:
                yield i
                if i != n //i:
                    yield n//i

    for m in yakusu():
        m -= 1
        if m == 0:
            continue

        if n // m == n % m:
            yield m

print(sum(main()))