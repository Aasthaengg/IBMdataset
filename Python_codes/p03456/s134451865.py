#ABC 086

a,b = map(int, input().split())
ans = []
for i in range(1,10001):
    ans.append(i**2)

sum = int(str(a) + str(b))
if sum in ans:
    print("Yes")
else:
    print("No")
