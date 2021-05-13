def actual(s):
    if len(set(s)) == len(s):
        return 'yes'

    return 'no'

s = input()
print(actual(s))