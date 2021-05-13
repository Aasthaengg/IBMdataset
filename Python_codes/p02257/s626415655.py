def main():
    n = int(input())
    count = 0
    for _ in range(n):
        x = int(input())
        count += isprime(x)
    print(count)

def isprime(x: int):
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for y in range(3, int(x**0.5)+1, 2):
        if x % y == 0:
            return False
    return True

if __name__ == '__main__':
    main()

