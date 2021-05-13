n = int(input())
d = sorted(list(map(int, input().split())))
l = len(d)

abc = d[:l//2]
arc = d[l//2:]

if abc[-1] == arc[0]:
    print(0)
    exit()
    
print(arc[0] - abc[-1])