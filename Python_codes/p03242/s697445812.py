N = list(input())
ans = ['1' if n == '9' else '9' for n in N]
print(''.join(ans))