N,H = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]
a_sort = sorted(AB,key=lambda x: x[0],reverse=True)
a_max = a_sort[0][0]

tmp = []
for a,b in AB:
    if b > a_max:
        tmp.append(b)

tmp.sort(reverse=True)

cnt = 0
for i in tmp:
    H -= i
    cnt += 1
    if H <= 0:
        print(cnt)
        exit()

print(H // a_max + cnt if H % a_max == 0 else H // a_max + 1 + cnt)