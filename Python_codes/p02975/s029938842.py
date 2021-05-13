N = int(input())
alist = list(map(int, input().split()))

ans = alist[0] ^ alist[1]
for a in alist[2:]:
    ans ^= a
if ans == 0:
    print("Yes")
else:
    print("No")
