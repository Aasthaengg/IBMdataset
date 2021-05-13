import collections
w = collections.Counter(input())
for i in w.values():
    if i%2 != 0:
        print("No")
        exit()
print("Yes")