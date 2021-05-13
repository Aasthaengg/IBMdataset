def solve(n, arr):
    # Firstly sort the array to reduce amount of calculation
    arr.sort()

    ans = 0

    for (i, _) in enumerate(arr):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if arr[i] != arr[j] and arr[i] != arr[k] and arr[j] != arr[k]:
                    if arr[i] + arr[j] > arr[k]:
                        ans += 1
    return ans


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split(' ')))
    print(solve(n, arr))