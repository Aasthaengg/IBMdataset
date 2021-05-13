def actual(n):
    s = str(n)

    if s[0] == s[1] == s[2] or s[1] == s[2] == s[3]:
        return 'Yes'
    return 'No'

    # if len(set(str(n))) <= 2:
    #     return 'Yes'
    #
    # return 'No'

s = input()
print(actual(s))