n = int(input())
x = list(range(n))
for i in range(n):
  x[i] = input()
c_0 = x.count("AC")
c_1 = x.count("WA")
c_2 = x.count("TLE")
c_3 = x.count("RE")
print("AC x {}".format(c_0))
print("WA x {}".format(c_1))
print("TLE x {}".format(c_2))
print("RE x {}".format(c_3))