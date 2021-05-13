a = int(input())
b = input().split()
ans = []
for x,y in zip(b[0],b[1]):
    ans += [x,y]
print("".join(ans))