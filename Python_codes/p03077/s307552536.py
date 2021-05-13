n = int(input())
T=[]
for i in range(5):
    T.append(int(input()))
mt=min(T)
ans = n//mt-1 if n%mt==0 else n//mt
ans += 5
print(ans)
