def solve(N, As):
    boxes = [-1 for _ in range(N + 1)]
    for k in range(N, 0, -1):
        s = 0
        for i in range(k + k, N + 1, k):
            s += boxes[i]
        s %= 2

        if s == As[k - 1]:
            boxes[k] = 0
        else:
            boxes[k] = 1
    boxes = boxes[1:]
    # print(boxes)
    m = sum(boxes)
    ans = []
    for i, b in enumerate(boxes):
        if b == 1:
            ans.append(str(i + 1))
    return "\n".join([str(m), " ".join(ans)])


# print(solve(3, [1, 0, 0]))
# print(solve(5, [0, 0, 0, 0, 0]))
# print(solve(5, [0, 0, 0, 0, 1]))
# print(solve(5, [0, 0, 0, 1, 1]))
# print(solve(5, [0, 0, 1, 1, 1]))

# print(solve(4, [0, 0, 0, 0]))
# print(solve(4, [0, 0, 0, 1]))
# print(solve(4, [0, 0, 1, 1]))
# print(solve(4, [0, 1, 1, 1]))

if __name__ == "__main__":
    N = int(input())
    As = list(map(int, input().split(" ")))
    print(solve(N, As))
