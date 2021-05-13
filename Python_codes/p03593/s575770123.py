from collections import Counter
import numpy as np

h, w = map(int, input().split())
arr = [list(map(str, input().rstrip())) for _ in range(h)]

arr = sum(arr, [])

arr = Counter(arr)
arr = np.array(list(arr.values()))


def solve(arr):
    # 偶数×偶数なら、制約がかなりきつい
    if h % 2 == 0 and w % 2 == 0:
        return np.all(arr % 4 == 0)

    # 奇数×奇数なら、
    elif h % 2 == 1 and w % 2 == 1:
        even = (h + w) // 2 - 1
        if (arr % 2 == 1).sum() != 1:
            return False
        odd = arr[np.where(arr % 2 == 1)].sum()
        if odd % 4 == 3:
            even -= 1
        arr = arr[np.where(arr != odd)]
        ans = (arr % 4 == 2).sum() <= even
        ans &= np.all(arr[np.where(arr % 4 != 2)] % 4 == 0)
        return ans

    #　どちらかの辺が偶数なら
    else:
        even = h // 2 if h % 2 == 0 else w // 2
        ans = (arr % 4 == 2).sum() <= even
        ans &= np.all(arr[np.where(arr % 4 != 2)] % 4 == 0)
        return ans


print("Yes" if solve(arr) else "No")