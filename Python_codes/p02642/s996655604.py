import collections


if __name__ == "__main__":
    N = int(input())
    A = [int(x) for x in input().split(" ")]
    counter = collections.Counter(A)

    duplicates = [key for key, val in counter.items() if val >= 2]
    A = [key for key in counter]

    A.sort()
    max_a = A[-1]
    multiples = set()
    ans = []

    for a in A:
        if a not in multiples:
            ans.append(a)
            for i in range(1, 10 ** 9):
                if a * i > max_a:
                    break
                multiples.add(a * i)

    print(len(set(ans) - set(duplicates)))