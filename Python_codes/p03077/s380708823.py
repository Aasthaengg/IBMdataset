N = int(input())
a = []
for i in range(5):
    a.append(int(input()))
if N % min(a) == 0:
    ans = N//min(a)+4
else:
    ans = N//min(a)+5
print(ans)
    
