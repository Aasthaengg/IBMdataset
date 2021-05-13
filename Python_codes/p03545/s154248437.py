abcd = str(input())
w = ["+","-"]
s = []
for i in w:
    for h in w:
        for j in w:
            num = int(abcd[0])
            l = [i,h,j]
            for k in range(len(l)):
                if l[k] == "+":
                    num += int(abcd[k+1])
                else:
                    num -= int(abcd[k+1])
            if num == 7:
                s.append(abcd[0]+i+abcd[1]+h+abcd[2]+j+abcd[3]+"="+"7")
print(s[0])