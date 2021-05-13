n = int(input())
res = 0
numa = numb = numboth = 0
for _ in range(n):
    s = input()
    res += s.count("AB")
    if s[0] == "B" and s[-1] == "A":
        numboth += 1
    elif s[0] == "B":
        numb += 1
    elif s[-1] == "A":
        numa += 1

#print(numboth, numa, numb)
#print(res)

if numboth == 0:
    res += min(numa, numb)
else:
    if numa == 0 and numb == 0:
        res += numboth - 1
    else:
        res += numboth
        res += min(numa, numb)
print(res)