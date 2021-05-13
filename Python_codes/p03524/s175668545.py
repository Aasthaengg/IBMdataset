from collections import Counter
s = [a for a in str(input())]
ss = dict((Counter(s)))
abc = ["a","b","c"]
check = True
try:
  for i in abc:
    if ss[i] < (len(s) // 3) or ss[i] > (len(s) // 3 + 1):
      check = False
except:
  if max(ss.values()) >= 2:
    check = False
print("YES" if check else "NO")