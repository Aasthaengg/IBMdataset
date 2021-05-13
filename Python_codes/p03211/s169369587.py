import sys

def main():
    S = list(input().rstrip())
    diffs = []
    for i in range(len(S) - 2):
        diffs.append(abs(753 - int("".join(S[i:i+3]))))
    print(min(diffs))


if __name__ == '__main__':
    main()
