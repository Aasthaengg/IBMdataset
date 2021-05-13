# CODE FESTIVAL 2016 予選 C: A – CF
s = input()
print('Yes' if 'C' in s and 'F' in s[s.index('C') + 1:] else 'No')