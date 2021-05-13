S = input()
c = S.count("0")
l = len(S)
print(l-abs(c-(l-c)))