s = input()
ans = s.rjust(15, 'o').count('o')  >=  8
print(ans and 'YES' or 'NO')