from collections import Counter

l=[x for x in input()];n=len(set(l));
c=Counter(l)
ans=[x for x in c.values() if x%2!=0]
print ("No" if len(ans)>0 else "Yes")