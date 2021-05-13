s = sorted(input())
t = sorted(input(), reverse=True)
sSort = ''.join(s)
tSortRev = ''.join(t)
if sSort < tSortRev:
    print("Yes")
else:
    print("No")