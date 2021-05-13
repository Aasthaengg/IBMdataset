from collections import Counter


def main():
    n = int(input())
    s = [input() for _ in range(n)]
    counter = Counter(s)
    most_common = counter.most_common()
    max_num = most_common[0][1]
    values, counts = zip(*most_common)
    for i, cnt in enumerate(counts):
        if cnt != max_num:
            last_index = i
            break
    else:
        last_index = len(counter)
    ans = list(values[:last_index])
    ans.sort()
    print("\n".join(ans))


if __name__ == "__main__":
    main()
