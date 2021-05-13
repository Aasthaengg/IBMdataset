s = input()

l = len(s)

if l%2 ==1: #偶数にする
    s = s[:-1]
else:
    s = s[:-2]



for i in range(l):
    l = len(s)
    lh = int(l/2)
    if s[:lh] == s[lh:]:
        break
    s = s[:-2]
    
print(len(s))
