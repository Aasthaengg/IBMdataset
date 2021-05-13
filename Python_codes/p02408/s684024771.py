#coding:UTF-8

n = input()
arr = {'S':range(13),'H':range(13),'C':range(13),'D':range(13)}

for i in range(n):
    a,b = raw_input().split()
    b = int(b)
    arr[a][b-1] = 14

for j in ['S','H','C','D']:
    for k in range(13):
        if arr[j][k] == 14:
            continue
        print j+" "+str(k+1)