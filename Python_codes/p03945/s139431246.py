import sys
s = input()

if all([x == s[0] for x in s]):
    print(0)
    sys.exit()

bw = s.count("BW")
wb = s.count("WB")

print(bw + wb)