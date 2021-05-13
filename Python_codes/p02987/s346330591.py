from collections import Counter
s = input()
S = Counter(s).most_common()
print('Yes' if S[0][1] == 2 and S[1][1] == 2 else 'No')