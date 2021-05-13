n = int(input())


def binary_search(n) -> int:
    target = n * 2
    left, right = 0, target
    while right - left != 1:
        mid = (left + right) // 2
        if mid * mid + mid < target:
            left = mid
        elif mid * mid + mid > target:
            right = mid
        elif mid * mid + mid == target:
            return mid
    return right


print(binary_search(n))
