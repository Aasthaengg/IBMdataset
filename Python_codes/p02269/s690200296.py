n = int(input())
dic = {}
ans = []

for i in range(n):
    com = input().split()
    c = com[0]

    if com[1] in dic:
        if c[0] == 'f': ans.append("yes")
        else: pass

    else:
        if c[0] == 'i': dic[ com[1] ] = i
        else: ans.append("no")


for i in ans: print(i)

