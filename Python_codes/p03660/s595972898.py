import queue
n = int(input())
way = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int,input().split())
    way[a].append(b)
    way[b].append(a)

qf = queue.Queue()
qs = queue.Queue()
qf.put(1)
qs.put(n)
who = ["" for i in range(n+1)]
wht = [10**5+5 for i in range(n+1)]
who[0] = "N"
who[1] = "F"
who[n] = "S"
wht[0] = 0
wht[1] = 0
wht[n] = 1


while not(qf.empty() and qs.empty()):
    if not qf.empty():
        fi = qf.get()
        if who[fi] == "F":
            for i in way[fi]:
                if wht[i] > wht[fi] + 2:
                    qf.put(i)
                    wht[i] = wht[fi] + 2
                    who[i] = "F"
    if not qs.empty():
        si = qs.get()
        if who[si] == "S":
            for i in way[si]:
                if wht[i] > wht[si] + 2:
                    qs.put(i)
                    wht[i] = wht[si] + 2
                    who[i] = "S"

if who.count("F") > who.count("S"):
    print("Fennec")
else:
    print("Snuke")
