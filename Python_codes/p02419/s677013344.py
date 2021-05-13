w = input().lower()
cnt = 0
while True:
    str = input().split()
    if str[0] == "END_OF_TEXT":
        break
    else:
        for i in range(len(str)):
            if w == str[i].lower():
                cnt += 1
print(cnt)