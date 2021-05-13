def actual(n, a):
    if n % 500 <= a:
        return 'Yes'

    return 'No'

n = int(input())
a = int(input())

print(actual(n, a))