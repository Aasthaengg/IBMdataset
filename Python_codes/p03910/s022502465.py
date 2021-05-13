N = int(input())
cnt = 0
now = 0
while True:
    now +=1
    cnt += now
    if cnt >=N:
        break
for i in range(1,now+1):
    if i == cnt-N:
        continue
    else:
        print(i)
