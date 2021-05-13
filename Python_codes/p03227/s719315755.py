def a_measure(S):
    ans = ''
    if len(S) == 2:
        ans = S
    elif len(S) == 3:
        ans = S[::-1]
    return ans

S = input()
print(a_measure(S))