ans = 0
for i in range(1, int(input())+1):
    if i%2 and (8 == len([j for j in range(1, i+1) if i%j == 0])):
        ans += 1
print(ans)
