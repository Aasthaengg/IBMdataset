def is_even(s):
    if len(s) % 2 == 1:
        return False
    mid = len(s) // 2
    if s[:mid] == s[mid:]:
        return True
    return False

def main():
    S = input().strip()
    S = S[:len(S)-2]
    while len(S) > 2:
        if is_even(S):
            break
        else:
            S = S[:len(S)-2]
    print(len(S))

if __name__ == "__main__":
    main()