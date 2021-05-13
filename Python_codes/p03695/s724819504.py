def main():
    n = int(input())
    As = list(map(int, input().split()))
    nums = []
    rainbow = 0
    for A in As:
        num = A // 400
        if num < 8:
            if num not in nums:
                nums.append(num)
        else:
            rainbow += 1
    ans_max = len(nums)+rainbow
    ans_min = max(1, len(nums))
    print(ans_min, ans_max)


if __name__ == "__main__":
    main()
