K, X = map(int, input().split())

def check():
    if 500*K>=X:
        return 'Yes'
    return 'No'
print(check())