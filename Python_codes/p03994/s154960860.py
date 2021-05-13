def main():
    word = list(input())
    operation = int(input())
    cost = {}
    for i in range(26):
        cost[chr(ord("a") + i)] = ord("z") - ord("a") - i + 1
    for i in range(len(word)):
        if cost[word[i]] <= operation and word[i] != "a":
            operation -= cost[word[i]]
            word[i] = "a"
        else:
            continue
    if 0 < operation:
        word[-1] = chr((ord(word[-1]) - ord("a") + operation % 26) % 26 + ord("a"))
    print("".join(word))


if __name__ == '__main__':
    main()

