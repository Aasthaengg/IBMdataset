n = int(raw_input())

point = [0, 0]
for i in range(n):
    word = map(str, raw_input().split())
    if word[0] == word[1]:
        point[0] += 1
        point[1] += 1
    elif len(word[0]) >= len(word[1]):
        for j in range(len(word[1])):
            if word[0][j] == word[1][j]:
                if j == len(word[1])-1:
                    point[0] += 3
                continue
            elif word[0][j] > word[1][j]:
                point[0] += 3
                break
            else:
                point[1] += 3
                break
    else:
        for j in range(len(word[0])):
            if word[0][j] == word[1][j]:
                if j == len(word[0])-1:
                    point[1] += 3
                continue
            elif word[0][j] > word[1][j]:
                point[0] += 3
                break
            else:
                point[1] += 3
                break
print "%d %d" % (point[0], point[1])