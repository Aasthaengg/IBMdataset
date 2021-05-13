li = list(map(int,input().split()))
check = [1,4,7,9]
dic = {1:0, 4:0, 7:0, 9:0}

for i in range(4):
    if li[i] in check:
        dic[li[i]] += 1
    else:
        print("NO")
        exit()

for j in check:
    if dic[j] != 1:
        print("NO")
        exit()
print("YES")

