n = int(input())
a0 = list(map(int,input().split()))
t = 0
for i in a0:
    t ^= i
ans = []
for i in a0:
    ans.append(str(t^i))
print(" ".join(ans))