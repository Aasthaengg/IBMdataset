s = input()
t = input()
flg = any(s[-i:] + s[: len(s) - i] == t for i in range(1, len(s) + 1))
print(["No", "Yes"][flg])