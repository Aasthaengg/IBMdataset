S = input()
a = [s for s in "abcdefghijklmnopqrstuvwxyz"]

for s in list(set(S)):
    if(s in a):
        a.remove(s)
if(a == []):
    print("None")
else:
    print(a[0])