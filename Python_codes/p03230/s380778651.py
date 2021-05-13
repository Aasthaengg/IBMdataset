# 基本形に追加するのを考える
# [1 2] [2 3] [1 3] の基本形にそれぞれ新しく1つずつ追加するとすると [1 2 4] [2 3 5] [1 3 6] [4 5 6]
# n=10だと
# [1 3 5 7] [1 2 6 8] [2 3 4 9 ] [4 5 6 10] [7 8 9 10]
# これに新しいのを加えるとするとすでにある5つを新規に導入するので 15
# [1 3 5 7 11] [1 2 6 8 12] [2 3 4 9 13] [4 5 6 10 14] [7 8 9 10 15] [11 12 13 14 15]
n = int(input())
if n == 1:  # これマジで理不尽
    print("Yes")
    print(2)
    print("1 1")
    print("1 1")
    exit()
anss = [[1, 2], [2, 3], [1, 3]]
target, length = 3, 3
while target <= n:
    if target == n:
        print("Yes")
        print(length)
        for ans in anss:
            b = " ".join(list(map(str, ans)))
            print(f"{len(ans)} {b}")
        exit()
    nex = list(range(target + 1, target + length + 1))
    for i, ans in enumerate(anss):
        ans.append(nex[i])
    anss.append(nex)
    target += length
    length += 1
print("No")