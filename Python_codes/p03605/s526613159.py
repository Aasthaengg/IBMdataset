def actual(N):
    if '9' in str(N):
        return 'Yes'

    return 'No'

N = int(input())
print(actual(N))