n = int(input())

for k in range(1,n + 2):
    if k * (k - 1)  == 2 * n:
        print("Yes")
        break
    if k * (k - 1) > 2 * n:
        print("No")
        exit()

print(k)
answer = [[] for _ in range(k)]

num = [[i,j] for i in range(k) for j in range(i+1,k)]

for i,st in enumerate(num):
    s,t = st
    answer[s].append(i + 1)
    answer[t].append(i + 1)

for ans in answer:
    print(k-1,*ans)
