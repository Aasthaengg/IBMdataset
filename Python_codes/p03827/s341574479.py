N = int(input())
S = input()
sum = ""
li = []
for s in S:
    sum += s
    li.append(sum)

ic = 0
dc = 0
ma = 0
for l in li:
    ic = l.count("I")
    dc = l.count("D")
    ma = max(ma, ic - dc)
    
print(ma)