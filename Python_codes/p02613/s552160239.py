a = int(input())
b = [input() for i in range(a)]
print("AC x {}\nWA x {}\nTLE x {}\nRE x {}".format(b.count('AC'),b.count('WA'),b.count('TLE'),b.count('RE')))