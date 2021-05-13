A,B = map(int,input().split())

H = W = 100
Ans = ["#"*100 for i in range(50)] + ["."*100 for i in range(50)]
count = 0
i = 0
j = 0
while count < A-1:
    count += 1
    Ans[i] = Ans[i][:j] + "." + Ans[i][j+1:]
    if j == 98:
        i += 2
        j = 0
    else:
        j += 2

count = 0
i = 0
j = 0
while count < B-1:
    count += 1
    Ans[99-i] = Ans[99-i][:j] + "#" + Ans[99-i][j+1:]
    if j == 98:
        i += 2
        j = 0
    else:
        j += 2
print(*[H,W])
for i in range(H):
    print(Ans[i])