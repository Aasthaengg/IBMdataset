S = input()
def is_hitachi(S):
    hitachi = [
        'hi',
        'hihi',
        'hihihi',
        'hihihihi',
        'hihihihihi',
    ]
    if S in hitachi:
        return 'Yes'
    else:
        return 'No'

print(is_hitachi(S))
