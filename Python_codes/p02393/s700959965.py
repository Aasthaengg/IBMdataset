t = map(int, raw_input().split())
kaisu = len(t)

for i in range(kaisu-1):
    for j in range(i+1, kaisu) :
        if t[i] > t[j] :
            temp = t[i]
            t[i] = t[j]
            t[j] = temp

for i in range(kaisu):
    print "%d" %t[i] , 