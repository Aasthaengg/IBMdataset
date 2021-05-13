s = sorted(input())
t = sorted(input())
t.reverse()

st = [s, t]
if st == sorted(st) and s != t:
    print("Yes")
else:
    print("No")