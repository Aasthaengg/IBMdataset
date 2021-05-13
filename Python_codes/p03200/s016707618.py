S = list(input())

cnt = 0
b = 0
for s in S:
    if s == "B":
        b += 1
    else:
        cnt += b
        
print(cnt)