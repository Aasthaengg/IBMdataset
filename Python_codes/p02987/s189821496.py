S = sorted(list(input()))
bl = (S[0]==S[1] and S[1]!=S[2] and S[2]==S[3])

print('Yes' if bl == 1 else 'No')
