from collections import Counter
n = int(input())
d = Counter(list(map(int, input().split())))
if len(d) == 1:
    if d[0] == n:
        print("Yes")
        exit()
elif len(d) == 2:
    if n%3 == 0 and d[0] == n//3:
        print("Yes")
        exit()
elif len(d) == 3:
    k = list(d.keys())
    if n%3 == 0 and k[0] ^ k[1] ^ k[2] == 0 and d[k[0]] == d[k[1]] == d[k[2]]:
        print("Yes")
        exit()
print("No")