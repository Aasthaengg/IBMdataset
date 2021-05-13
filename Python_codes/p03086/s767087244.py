s = str(input())
mx = 0
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        cnt = j-i
        p = 0
        for k in list(s[i:j]):
            if k in ["A","C","G","T"]:
                p += 1
        if p == cnt:
            if p > mx:
                mx = p
print(mx)
