a,b = list(map(int,input().split()))
X = int(str(a)+str(b))
out = "No"
for i in range(1,X//2+1):
    if i**2==X:
        out="Yes"
        break
print(out)