s,c = map(int,input().split())

if s >= c:
    #print("s>=c")
    scc = int(c/2)
    print(scc)
    exit()

if s < c:
    #print("s<c")
    scc = s
    cc = c-s*2
    scc += int(cc/4)
    print(scc)
    exit()
