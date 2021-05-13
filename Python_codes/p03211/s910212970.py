s = str(input())
num = 10**9
for i in range(len(s)-2):
    t = abs(int(s[i:i+3])-753)
    if t < num:
        num = t
print(num)