from collections import Counter
S = input().rstrip()
dic = Counter(S)
print("Yes" if list(dic.values())==[2,2] else "No")
