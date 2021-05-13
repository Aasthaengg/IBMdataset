s=input()
print('NYOE S'[any([s[:i]=='keyence'[:i] and s[len(s)-7+i:]=='keyence'[i:] for i in range(8)])::2])