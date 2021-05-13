s = input()
H = int(int(s / 60) / 60)
i = int(s / 60) % 60
s = s % (60 * 60) % 60
print str(H) + ":" + str(i) + ":" + str(s)