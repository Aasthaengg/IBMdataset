n = int(input())
al = list(map(int,input().split()))


from collections import defaultdict
dic = {}

for a in al:
    if a not in dic:
        dic[a] = 0
    dic[a] += 1
if 0 in dic:
    if dic[0] == n:
        print("Yes")
        exit()
if 0 in dic:
    if n % 3 == 0:
        if dic[0] == 1 * n // 3:
            print("Yes")
            exit()
if n % 3 != 0:
    print("No")
    exit()
else:
    if len(dic) == 3:
        if max(dic.values()) == n // 3:
            a = 0
            for i in dic:
                a ^= i
            if a == 0:
                print("Yes")
                exit()
print("No")


