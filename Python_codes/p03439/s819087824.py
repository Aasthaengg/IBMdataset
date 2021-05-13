import sys

N = int(input())
# 二分探索っぽい感じ
print("0")
sys.stdout.flush()
zero = input()
high = N - 1
low = 0
if zero != "Vacant":
    while True:
        mid = (high + low) // 2
        print(mid)
        sex = input()
        if sex == "Vacant":
            break
        if (mid % 2 == 0 and sex == zero) or (mid % 2 == 1 and sex != zero):
            low = mid + 1
            # zero -> midには存在しない
        else:
            high = mid - 1


