n = int(input())

s={}

s["AC"] = 0
s["WA"] = 0
s["TLE"] = 0
s["RE"] = 0


for i in range(n):
    r = input()
    s[r] += 1


print('AC x ' + str(s["AC"]))
print('WA x ' + str(s["WA"]))
print('TLE x ' + str(s["TLE"]))
print('RE x ' + str(s["RE"]))

