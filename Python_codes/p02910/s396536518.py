S = input()

print('No' if('L' in set(S[::2]) or 'R' in set(S[1::2])) else 'Yes')
