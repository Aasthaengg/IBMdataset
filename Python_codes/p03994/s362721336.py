def main():
    s = input()
    K = int(input())
    new_s = ""

    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    d = {
        "a": 0,
        "b": 25,
        "c": 24,
        "d": 23,
        "e": 22,
        "f": 21,
        "g": 20,
        "h": 19,
        "i": 18,
        "j": 17,
        "k": 16,
        "l": 15,
        "m": 14,
        "n": 13,
        "o": 12,
        "p": 11,
        "q": 10,
        "r": 9,
        "s": 8,
        "t": 7,
        "u": 6,
        "v": 5,
        "w": 4,
        "x": 3,
        "y": 2,
        "z": 1,
    }

    for i in range(len(s)-1):
        if d[s[i]] <= K:
            K -= d[s[i]]
            new_s += 'a'
        else:
            new_s += s[i]

    new_s += l[(l.index(s[-1]) + K) % 26]

    print(new_s)

if __name__ == '__main__':
    main()
