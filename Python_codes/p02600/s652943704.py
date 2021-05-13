x = int(input())
cnt = 6
while True:
    if x < cnt*100:
        break
    cnt += 2
print(int(11 - cnt / 2))