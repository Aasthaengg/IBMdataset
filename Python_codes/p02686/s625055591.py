n = int(input())
flag = 0
ML = []
MM = []
MR = []
L = 0
R = 0
for _ in range(n):
    s = input()
    saisho = 0
    cur = 0
    for w in s:
        if w == "(":
            cur += 1
        else:
            cur -= 1
            saisho = min(saisho, cur)
    if cur > 0:
        ML.append((saisho, cur))
    elif cur < 0:
        MR.append((-cur + saisho, -cur))
    else:
        MM.append((saisho, cur))
ML.sort(reverse=True)
MR.sort(reverse=True)
leftnow = 0
for saisho, delta in ML:
    if leftnow + saisho < 0:
        flag = 1
    leftnow += delta
for saisho, delta in MM:
    if leftnow + saisho < 0:
        flag = 1
    leftnow += delta
rightnow = 0
for saisho, delta in MR:
    if rightnow + saisho < 0:
        flag = 1
    rightnow += delta

if rightnow != leftnow:
    flag = 1
if flag:
    print("No")
else:
    print("Yes")
