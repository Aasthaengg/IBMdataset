s = list(input())
s = list(map(int,s))
k = int(input())
for _ in s[:k]:
    if _ != 1:
        print(_)
        exit(0)
print(1)