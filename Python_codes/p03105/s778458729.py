A, B, C = map(int, input().split())
for i in range(C+1):
    if A*(i+1) <=B:
        continue
    else:
        break
print(i)