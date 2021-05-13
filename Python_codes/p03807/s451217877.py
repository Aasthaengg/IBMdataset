input()
A = map(int,input().split())
odd = 0
for a in A:
    if a%2!=0:
        odd+=1
print("NO" if odd%2!=0 else "YES")