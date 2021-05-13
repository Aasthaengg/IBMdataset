x, n = map(int, input().split())
p = list(map(int, input().split()))
l = sorted(p)
new = []
t = x in l

if t == False:
    re = x #n = 0でよかった。ここでは、listの中にxがなかったときにreにxを入れている。
else:
    for i in range(len(l)):
        TorF_1 = x + i + 1 in l
        TorF_2 = x - i - 1 in l
        if TorF_2 == False:
            re = x - i - 1
            break

        elif TorF_1 == False:
            re = x + i + 1
            break
    
print(re)
