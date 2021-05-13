string = "{0}KIH{1}B{2}R{3}"
OK = []
for i in range(2**4):
    ins_a = [""]*4
    for j in range(4):
        if ((i >> j) & 1):
            ins_a[j] = "A"
    OK.append(string.format(*ins_a))
if input() in OK:
    print("YES")
else:
    print("NO")