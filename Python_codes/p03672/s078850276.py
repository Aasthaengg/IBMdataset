from sys import exit

s = input()

for i in range(len(s)-1, -1, -1):
    if i % 2 == 1:
        continue

    flag = True
    for j in range(i // 2):
        if s[j] != s[i//2+j]:
            flag = False
    
    if flag:
        print(i)
        exit()