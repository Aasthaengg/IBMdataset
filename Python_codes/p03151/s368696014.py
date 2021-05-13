import sys
n = int(input())
a_li = list(map(int,input().split()))
b_li = list(map(int,input().split()))

if sum(a_li)<sum(b_li):
    print(-1)
    sys.exit()

amari_li = []
tarinai_li = []

for  a,b in zip(a_li,b_li):
    if a >= b:
        amari_li.append(a-b)
    else:
        tarinai_li.append(b-a)

t = sum(tarinai_li)

#print(amari_li,tarinai_li)

if len(tarinai_li) == 0:
    print(0)
    sys.exit()

amari_li.sort(reverse=True)
count = 0
for a in amari_li:
    t -= a
    count += 1
    if t <= 0:
        break
print(count+len(tarinai_li))