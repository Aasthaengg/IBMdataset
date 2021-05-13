count = int(input())
list = []
for i in range(count):
  list.append(input())
a = list.count("AC")
b = list.count("WA")
c = list.count("TLE")
d = list.count("RE")
print("AC x " + str(a))
print("WA x " + str(b))
print("TLE x " + str(c))
print("RE x " + str(d))