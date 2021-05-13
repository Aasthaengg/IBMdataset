def resolve():
    ans = [input() for _ in range(5)]
    an = 0
    count = []
    for i in range(5):
        if ans[i][-1]=="0":
            an += int(ans[i])
        else:
            an += int(ans[i])+10-int(ans[i][-1])
            count.append(int(ans[i][-1]))
    print(an-10+min(count) if len(count) != 0 else an)
resolve()