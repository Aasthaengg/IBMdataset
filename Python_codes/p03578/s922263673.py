n = int(input())
d = list(map(int,input().split()))
m = int(input())
t = list(map(int,input().split()))
dic1 = {}
dic2 = {}
for i in d:
    if i in dic1:
        dic1[i] += 1
    else:
        dic1[i] = 1
for i in t:
    if i in dic2:
        dic2[i] += 1
    else:
        dic2[i] = 1
for i in t:
    if i not in dic1:
        print("NO")
        exit()
    elif dic1[i] < dic2[i]:
        print("NO")
        exit()
print("YES")