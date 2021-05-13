N = int(input())


def is_male(res):
    return True if res == 'Male' else False

l = 0
h = N
print(l)
prev_sex = is_male(input())
while True:
    print((h + l) // 2)
    res = input()
    if res == 'Vacant':
        break
    sex = is_male(res)
    if (((h + l) // 2 - l) % 2 == 0 and sex != prev_sex) or (((h + l) // 2 - l) % 2 == 1 and sex == prev_sex):
        h = (h + l) // 2
    else:
        l = (h + l) // 2
        prev_sex = sex
