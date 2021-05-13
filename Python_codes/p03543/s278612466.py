def check():
    S = list(input())
    if len(set(S[:-1]))==1 or len(set(S[1:]))==1:
        return 'Yes'
    return 'No'
print(check())