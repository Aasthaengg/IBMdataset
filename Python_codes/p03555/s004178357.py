def actual(s1, s2):
    if s1[0] == s2[2] and s1[1] == s2[1] and s1[2] == s2[0]:
        return 'YES'

    return 'NO'


s1 = input()
s2 = input()
print(actual(s1, s2))
