b,w=map(int,input().split())
H = 100
bc = wc = 1
print(100,100)
for i in range(H):
    s=""
    for j in range(H):
        if i < 50:
            if i %2!=0 and j%2!=0 and wc<w and j !=99:
                s+='#'
                wc+=1
            else:s+='.'
        else:
            if i %2!=0 and j%2!=0 and bc <b  and j!=99:
                s+='.'
                bc+=1
            else:s+='#'
    print(s)
