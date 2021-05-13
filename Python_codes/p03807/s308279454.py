def main():
    N = int(input())
    *A, = map(int, input().split())

    even = 0

    for a in A:
        if a % 2 == 0: even += 1

    odd = N - even

    if odd % 2 == 1:
        return False
    else:
        return True

print('YES' if main() else 'NO')