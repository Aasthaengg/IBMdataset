import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()

    is_keyence = False
    if S[:7] == "keyence":
        is_keyence = True
    elif S[-7:] == "keyence":
        is_keyence = True
    elif S[:1] == "k" and S[-6:] == "eyence":
        is_keyence = True
    elif S[:2] == "ke" and S[-5:] == "yence":
        is_keyence = True
    elif S[:3] == "key" and S[-4:] == "ence":
        is_keyence = True
    elif S[:4] == "keye" and S[-3:] == "nce":
        is_keyence = True
    elif S[:5] == "keyen" and S[-2:] == "ce":
        is_keyence = True
    elif S[:6] == "keyenc" and S[-1:] == "e":
        is_keyence = True

    ans = "YES" if is_keyence else "NO"
    print(ans)


if __name__ == "__main__":
    main()
