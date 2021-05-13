n = int(input())
butnum = {}
for i in range(1,n+1):
    butnum[i] = int(input())
pushbut = 1
pushedbut =[]
jud = 0
for j in range(1,n+1):
    pushbut = butnum[pushbut]
    if pushbut == 2:
        print(j)
        jud = 1
        break
if jud == 0:
    print(-1)