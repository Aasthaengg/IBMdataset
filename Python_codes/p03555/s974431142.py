def resolve():
    li = list()
    for i in range(2):
        line = input()
        li.append(line)
    ans = list()
    for i in range(2):
        line = li[1-i]
        al = line[2] + line[1] + line[0]
        ans.append(al)
    sp = ""
    for i in range(2):
        if ans[i] != li[i]:
            sp = "NO"
            break
    if sp != "NO":
        sp = "YES"
    print(sp)
resolve()