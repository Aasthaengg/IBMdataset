n = int(input())
l = list(map(int,input().split()))

anslist = []

while l:
    for i in range(len(l)-1,-1,-1):
        if l[i] == i+1:
            anslist.append(l.pop(i))
            break
    else:
        print(-1)
        exit()

anslist.reverse()
for i in anslist:
    print(i)