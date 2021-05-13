s = input()
k = int(input())

if len(set(s)) == 1:
    print(len(s)*k//2)
    exit()

tmp = list(s * 2)
for i in range(len(tmp)-1):
    if i < len(s) and tmp[i] == tmp[i+1]:
        tmp[i + 1] = "#"
    elif i >= len(s) and tmp[i] == tmp[i+1]:
        tmp[i + 1] = "#"

fst = tmp[:len(s)].count("#")
snd = tmp[len(s):].count("#")

if k == 1:
    print(fst)
else:
    print(fst + snd * (k-1))