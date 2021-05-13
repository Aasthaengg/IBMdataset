a=list(map(int, input().split()))
s=1
for i in range(5):
    if a[i]==0:
        s+=i
        break
print(s)