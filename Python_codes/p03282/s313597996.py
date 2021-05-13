s = list(input())
k = int(input())

cnt = 0
for i in range(len(s)):
    num = int(s[i])
    if num == 1:
        cnt += 1
        if cnt == k:
            print(num)
            break          
    else:
        print(num)
        break