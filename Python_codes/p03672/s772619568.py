l = list(input())
while len(l) > 0:
    l = l[:-2]
    if l[:len(l)//2] == l[len(l)//2:]:
        print(len(l))
        exit()