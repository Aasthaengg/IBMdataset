def main():
    N = int(input())
    S = input()

    return S.count('R') > S.count('B')

print('Yes' if main() else 'No')
