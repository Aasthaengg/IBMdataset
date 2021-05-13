s = input()
t = 0
for i in range(1,len(s)-1):
    t += 1
print(s[0] + str(t) + s[len(s)-1])