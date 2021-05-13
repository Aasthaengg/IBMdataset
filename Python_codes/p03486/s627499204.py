s = input()
t = input()
slst = []
tlst = []
for i in s:
  slst.append(i)
for i in t:
  tlst.append(i)
slst.sort(key=lambda x: ord(x))
tlst.sort(key=lambda x: ord(x), reverse=True)
s = ''.join(slst)
t = ''.join(tlst)
print('Yes' if s < t else 'No')