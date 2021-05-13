from collections import Counter
 
s = Counter(input())
t = Counter(input())
 
sv = sorted(s.values())
tv = sorted(t.values())
 

if sv == tv:
    print("Yes")
else:
    print("No")
