def actual(s):
    return s.count('+') - s.count('-')


s = input()
print(actual(s))