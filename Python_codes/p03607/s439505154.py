n = int(input())
A = [input() for _ in range(n)]
AS = set()
for i in A:
    if i not in AS:
        AS.add(i)
    else:
        AS.remove(i)
print(len(AS))