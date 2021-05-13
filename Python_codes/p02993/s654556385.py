a = input()

def func():
    for x in range(len(a) - 1):
        if a[x] == a[x + 1]:
            return 'Bad'

    return 'Good'

print(func())
