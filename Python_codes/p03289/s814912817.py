s = input()
flg1 = s[0] == "A"
flg2 = s[2:-1].count("C") == 1
s = s.replace("A", "")
s = s.replace("C", "")
flg3 = s.islower()
print(["WA", "AC"][flg1 and flg2 and flg3])