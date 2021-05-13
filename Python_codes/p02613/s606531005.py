hashmap = {"AC":0, "WA":0, "TLE":0, "RE":0}
a = int(input())
for i in range(a):
    hashmap[str(input())] += 1
print("AC x " + str(hashmap["AC"]))
print("WA x " + str(hashmap["WA"]))
print("TLE x " + str(hashmap["TLE"]))
print("RE x " + str(hashmap["RE"]))