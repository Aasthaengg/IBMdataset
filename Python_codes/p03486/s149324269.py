s = sorted(list(input().strip()))
t = sorted(list(input().strip()),reverse=True)
if s<t:
    print("Yes")
else:
    print("No")