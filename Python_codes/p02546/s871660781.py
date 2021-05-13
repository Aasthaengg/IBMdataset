def actual(s: str) -> str:
    tail = s[-1]

    if tail == 's':
        return s + 'es'
    else:
        return s + 's'

s = input()
print(actual(s))