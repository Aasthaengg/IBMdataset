num = int(input())
input_line = list(map(int,input().split(' ')))

bb = 0
bi = 0

for i in input_line:
    if(i==(bi+1)):
        bi += 1
    else:
        bb += 1
if(bi>0):
    print(bb)
else:
    print(-1)
