k = int(input())

sho = k // 50
amr = k%50

ans = []

print(50)
for i in range(50):
    if i < amr:
        ans.append(sho+1+49)
    else:
        ans.append(sho-amr+49)
        
print(*ans)