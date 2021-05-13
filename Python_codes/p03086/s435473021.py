ans = 0
c = 1
li = ["A","C","G","T"]
s = input()
lens = len(s)
for i in range(lens):
    for j in range(lens-(i)):
        a = s[j:j+i+1]
        for k in range(i+1):
            if a[k] not in li:
                c = 1
                break
            else:
                c = 0
                continue
        if c == 0:
            ans = i+1
        else:
            c = 1
print(ans)