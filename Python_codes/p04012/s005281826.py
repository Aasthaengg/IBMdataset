s = input()
flg = all([s.count(x) % 2 == 0 for x in set(s)])
print("Yes" if flg else "No")