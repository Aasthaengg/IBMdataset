N = int(input())
S = input()

middle = len(S) // 2

if S[:middle] == S[middle:]:
    print('Yes')
else:
    print('No')
