def main():
    A, B, C= list(map(int, input().split()))

    return  A == B == C

print('Yes' if main() else 'No')
