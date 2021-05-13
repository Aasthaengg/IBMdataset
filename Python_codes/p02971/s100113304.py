n = int(input())
l = []

for i in range(n):
    l.append(int(input()))

def has_duplicates(seq):
    return sorted(seq)[len(seq)-1] == sorted(seq)[len(seq)-2]

x = max(l)

if has_duplicates(l):
    for i in l:
        print(x)
else:
    for i in l:
        if i != x:
            print(x)
        else:
            print(sorted(l)[n-2])