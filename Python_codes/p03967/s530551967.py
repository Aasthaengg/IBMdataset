def main():
    S = input()
    m = len(S) // 2
    print(-S[:len(S) - m].count('p') + S[len(S) - m:].count('g'))

main()
