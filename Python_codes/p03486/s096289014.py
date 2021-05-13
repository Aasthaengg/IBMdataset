s = sorted(input())
t = sorted(input(),reverse=True)

ts = [t, s]
if ts != sorted(ts):
    print("Yes")
else:
    print("No")