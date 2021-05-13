from string import ascii_lowercase

def main():
    s = list(input())
    K = int(input())
    for i, c in enumerate(s):
        num = ord(c) - ord("a")

        if num > 0 and K - (26-num) >= 0:
            s[i] = "a"
            K -= (26-num)

    num = ord(s[-1]) - ord("a")
    last = (num + K)%26
    s[-1] = ascii_lowercase[last]
    print("".join(s))

        
if __name__ == "__main__":
    main()