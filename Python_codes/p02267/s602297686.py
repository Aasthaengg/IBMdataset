n1 = int(input())
s = (input()).split()
n2 = int(input())
t = (input()).split()
m = []

for i in range(0, n2):
      key = t[i]
      for j in range(0, n1):
            if s[j] == t[i]:
                  m.append(s[j])
                  break
print(len(m))