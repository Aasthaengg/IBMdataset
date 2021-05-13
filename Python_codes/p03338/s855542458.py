def answer(n: int, s: str) -> int:
    result = 0
    for i in range(1, n):
        x = set(s[i:])
        y = set(s[:i])
        common_characters = x.intersection(y)
        result = max(result, len(common_characters))

    return result

def main():
    n = int(input())
    s = input()
    print(answer(n,s))

if __name__ == '__main__':
    main()
