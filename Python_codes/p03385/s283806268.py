def actual(s):
    if set(s) == {'a', 'b', 'c'}:
        return 'Yes'

    return 'No'

s = input()
print(actual(s))