n = int(input())
a = []
for _ in range(n):
    a.append(input())
print("AC x {}".format(a.count("AC")))
print("WA x {}".format(a.count("WA")))
print("TLE x {}".format(a.count("TLE")))
print("RE x {}".format(a.count("RE")))