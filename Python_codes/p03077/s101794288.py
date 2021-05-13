n = int(input())
abc = []
res = [0]*5
for i in range(5):
    a = int(input())
    abc.append(a)
    res[i] = -(-n//a)
ans = 4 + max(res)
print(ans)