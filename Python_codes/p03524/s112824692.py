from collections import Counter
s = input()
s_counter = Counter(s)
s = [0]*3
s[0] = s_counter["a"]
s[1] = s_counter["b"]
s[2] = s_counter["c"]
if max(s)-min(s) >= 2:
    print("NO")
else:
    print("YES")