n = int(input())

s = list()
for i in range(n):
    s.append(input())

print("AC x {}".format(s.count("AC")))
print("WA x {}".format(s.count("WA")))
print("TLE x {}".format(s.count("TLE")))
print("RE x {}".format(s.count("RE")))
