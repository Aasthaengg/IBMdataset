h = int(input())
cnt = 1
while 1 < h:
    cnt += 1
    h //= 2
    #print(h)
#print(cnt)

res = 0

for v in range(cnt):
    res += 2**v
print(res)