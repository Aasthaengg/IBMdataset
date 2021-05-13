s = input()
w = ["R","RR","RRR"]
ans = 0

for i in range(3):
    if w[i] in s:
        ans = i + 1
        
print(ans)