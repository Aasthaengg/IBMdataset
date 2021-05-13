K = int(input())
s = input()
ans = ''.join(list(s)[:K])
print(ans.ljust(K+3, '.') if s != ans else s)
