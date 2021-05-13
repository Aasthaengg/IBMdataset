s = input()
l = []
ans = 0
ans_l = []
for i in range(len(s)-2):
    l.append(s[i:i+3])
for i in l:
    ans = abs(int(i)-753)
    ans_l.append(ans)
print(min(ans_l))