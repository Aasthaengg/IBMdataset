n = int(input())
li = [0]*5
for i in range(n):
    s = input()
    if s[0] == "M":
        li[0] += 1
    elif s[0] == "A":
        li[1] += 1
    elif s[0] == "R":
        li[2] += 1
    elif s[0] == "C":
        li[3] += 1
    elif s[0] == "H":
        li[4] += 1
total = li[0]*li[1]*li[2] + li[0]*li[1]*li[3] + li[0]*li[1]*li[4] + li[0]*li[2]*li[3] + li[0]*li[2]*li[4] + li[0]*li[3]*li[4] + li[1]*li[2]*li[3] + li[1]*li[2]*li[4] + li[1]*li[3]*li[4] + li[2]*li[3]*li[4]
print(total)