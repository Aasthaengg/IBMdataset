n = int(input())
h = list(map(int, input().split()))

def mizuyari(l):
    if l == 0 or l == []:
        return 0
    nin = min(l)
    for i in range(len(l)):
        l[i] -= nin
    index = l.index(0)
    return nin + mizuyari(l[:index]) + mizuyari(l[index+1:])


print(mizuyari(h))