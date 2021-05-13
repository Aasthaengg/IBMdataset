#  Copyright: this code was written at 2019. for AtCoder by Silviase
s = input()
tf = [True, False]
f = False
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                for m in range(2):
                    tmp = ""
                    if tf[i]:
                        tmp += "A"
                    tmp += "KIH"
                    if tf[k]:
                        tmp += "A"
                    tmp += "B"
                    if tf[l]:
                        tmp += "A"
                    tmp += "R"
                    if tf[m]:
                        tmp += "A"
                    if tmp == s:
                        f = True
print("YES" if f else "NO")
