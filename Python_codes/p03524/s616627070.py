s=input()
ct={"a":0,"b":0,"c":0}
for i in range(len(s)):
  ct[s[i]]+=1
print("YES" if max(ct.values())-min(ct.values())<2 else "NO")