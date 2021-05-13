n = int(input())

lt = []
for _ in range(n):
    lt.append(tuple(map(int, input().split())))

for i in range(n-2):
    if len(set(lt[i])) == 1 and len(set(lt[i+1])) == 1 and len(set(lt[i+2])) == 1:
        print("Yes")
        exit(0)
print("No")
