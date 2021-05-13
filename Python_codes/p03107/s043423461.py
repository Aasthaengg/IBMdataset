s = input()
n0 = s.count('0')
n1 = s.count('1')
ans = min(n0,n1) * 2
print(ans)