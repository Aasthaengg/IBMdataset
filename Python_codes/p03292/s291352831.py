li = sorted(list(map(int,input().split())))

li_2 = [li[2] - li[1],li[1] - li[0]]

print(sum(li_2))
