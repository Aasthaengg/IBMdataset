def check():
    N = list(input())
    for i in range(2):
        if len(set(N[i:i+3]))==1:
            return 'Yes'
    return 'No'
print(check())