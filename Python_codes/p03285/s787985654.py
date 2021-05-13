N=int(input())
ans=False
for i in range(100):
    for j in range(100):
        if 4*i+7*j==N:
            ans=True
out="Yes" if ans else "No"
print(out)
