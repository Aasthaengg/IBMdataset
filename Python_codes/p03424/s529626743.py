n = int(input())
s = list(map(str, input().split()))
dic = {'P':0, 'W':0, 'G':0, 'Y':0}
for i in range(n):
    dic[s[i]] += 1
cnt = 0
for i in dic.keys():
    if dic[i] > 0:
        cnt += 1
if cnt == 3:
    print("Three")
elif cnt == 4:
    print("Four")