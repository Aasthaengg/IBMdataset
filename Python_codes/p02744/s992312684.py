n = int(input())

before = ["0"]
for i in range(n-1):
    next = []
    for elem in before:
        m = 1
        for j in range(len(elem)):
            m = max(m, int(elem[j])+1)
        for j in range(m+1):
            next.append(elem+str(j))
    before = next[:]

before.sort()
d = {"0":"a", "1":"b", "2":"c", "3":"d", "4":"e", "5":"f", "6":"g", "7":"h", "8":"i", "9":"j"}
for elem in before:
    ans = []
    for i in range(len(elem)):
        ans.append(d[elem[i]])
    print("".join(ans))
