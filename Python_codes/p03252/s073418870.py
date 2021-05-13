from collections import*
s,t=Counter(input()),Counter(input())
print("YNeos"[sorted(s.values())!=sorted(t.values())::2])