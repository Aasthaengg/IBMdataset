n=int(raw_input())

tarou=0
hanako=0
for i in range(n):
    words=raw_input().split(" ")
    tarou_sum = 0
    hanako_sum = 0
    for idx, c in enumerate(words[0]):
        
        if len(words[1]) -1 < idx:
            tarou += 3
            break
        
        if ord(words[1][idx]) < ord(c):
            tarou += 3
            break
        elif ord(words[1][idx]) > ord(c):
            hanako += 3
            break
        else:
            continue
    else:
        if len(words[0]) < len(words[1]):
            hanako += 3
        else:
            tarou += 1
            hanako += 1

print "%d %d" % (tarou, hanako)