# tenka1-2018D - Crossing
"""
if N = K(K + 1)/2 -> Yes
construct a triangle(e.g. N = 10, K = 4):
    1 0 0 0
    2 3 0 0
    4 5 6 0
    7 8 9 10
the answer will be:
  {each row until 0 + column straight down from there}
    {1 2 4 7}
    {2 3 5 8}
    {4 5 6 9}
    {7 8 9 10}
  {diagonal line}
    {1 3 5 10}
"""
def main():
    N = int(input())
    K = int((N * 2) ** 0.5)
    if K * (K + 1) / 2 != N:
        print("No")
        return
    row, cur, cnt = [], 1, 1
    while cur + cnt - 1 <= N:
        row.append(list(range(cur, cur + cnt)) + [0] * (K - cnt))
        cur += cnt
        cnt += 1
    col = [list(c) for c in zip(*row)]
    ans, diag = [], []  # diag: diagonal line
    for i, (r, c) in enumerate(zip(row, col)):
        diag.append(r[i])
        ans.append(r[:i] + c[i:])
    ans.append(diag)
    print("Yes", K + 1, sep="\n")
    for a in ans:
        print(K, end=" ")
        print(" ".join(map(str, a)))


if __name__ == "__main__":
    main()