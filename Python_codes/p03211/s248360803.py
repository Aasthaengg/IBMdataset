s = input()
a = []
for i in range(len(s)-2):
  a.append(abs(int(s[i])*100+int(s[i+1])*10+int(s[i+2])-753))
print(min(a))