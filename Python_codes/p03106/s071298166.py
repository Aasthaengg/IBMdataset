a, b, k = map(int, input().split())

cnt = 0
for i in range(1, 200):
    if(a%i == 0 and b%i == 0):
        cnt = cnt + 1;

cnts = cnt - k + 1
cnt = 0
for i in range(1, 200):
    if(a%i == 0 and b%i == 0):
        cnt = cnt + 1;
    if(cnt == cnts):
        print(i)
        break
