N = int(input())

def judge(n):
    n *= 2
    for d in range(1,n):
        if n == d*(d+1):
            return True, d
    return False, -1

# k : 部分集合の大きさ
# k+1 : 部分集合の数
flag, k = judge(N)
if not flag:
    print("No")
    exit()

print("Yes")
print(k+1)

l = [[] for _ in range(k+1)]
c = 1
for i in range(k+1):
    for j in range(i+1, k+1):
        l[i].append(c)
        l[j].append(c)
        c += 1

for line in l:
    print(k, end = " ")
    print(*line)