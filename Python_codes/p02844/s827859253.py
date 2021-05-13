n = int(input())
s = input()
ans = 0
for i in range(1000):
    tmp = str(i).zfill(3)
    number = [tmp[0],tmp[1],tmp[2],"OK"]
    pos = 0
    for ss in s:
        if ss == number[pos] and pos < 3:
            pos += 1
    if number[pos] == "OK":
        ans += 1
print(ans)