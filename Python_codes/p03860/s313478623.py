str = input()

s = str.replace("AtCoder ", "").replace(" Contest", "")

s_capital = s[:1]

contest_abbr = 'A' + s_capital + 'C'

print(contest_abbr)
