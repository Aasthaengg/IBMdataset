def actual(N):
    s = str(N)

    if s == s[::-1]:
        return 'Yes'

    return 'No'

N = int(input())
print(actual(N))