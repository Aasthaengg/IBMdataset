strings = list(input().split())

flag = 'YES'
for i in range(2):
    if strings[i][-1] != strings[i+1][0]:
        flag = 'NO'
print(flag)