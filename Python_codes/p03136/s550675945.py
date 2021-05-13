import sys
lines = [s.rstrip("\n") for s in sys.stdin.readlines()]
n, = [int(num) for num in lines.pop(0).split(" ")]
l_list = [int(num) for num in lines.pop(0).split(" ")]
l_list.sort(reverse=True)
m = l_list.pop(0)
if m < sum(l_list):
    print("Yes")
else:
    print("No")
