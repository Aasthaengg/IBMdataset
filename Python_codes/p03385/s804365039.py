def main():
    S = input()
    if sorted(list(S)) == sorted(list('abc')):
        return True
    return False
if main():
    print('Yes')
else:
    print('No')

