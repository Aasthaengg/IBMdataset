S = input()
for i,c in enumerate(S):
    if c=='C': break
print('Yes' if 'F' in S[i+1:] else 'No')