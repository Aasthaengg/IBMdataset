n = int(input())
l = input().split()
ll = list(map(int, l))
if max(ll) < sum(ll) - max(ll):
    print("Yes")
else:
    print("No")
