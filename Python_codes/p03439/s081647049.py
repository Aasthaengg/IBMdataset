def val(num):
    print(num, flush=True)
    sex = input()
    if sex == "Vacant":
        exit(0)
    return 1 if sex == "Male" else 0


n = int(input())

l_sex = val(0)
r_sex = val(n - 1)

left = 0
right = n - 1

while left < right:
    mid = (left + right) // 2
    sex = val(mid)
    if (mid - left) % 2 == 0 and sex != l_sex:
        right = mid
        r_sex = sex
    elif (mid - left) % 2 == 1 and sex == l_sex:
        right = mid
        r_sex = sex
    else:
        left = mid
        l_sex = sex