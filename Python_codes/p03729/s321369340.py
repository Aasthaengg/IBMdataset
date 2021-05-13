s = input().split()
print('YES' if all(s[i][-1] == s[i+1][0] for i in range(2)) else 'NO')
