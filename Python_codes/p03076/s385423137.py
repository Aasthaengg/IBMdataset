R=[int(input()) for i in range(5)]
r=[]
p=10
for i in range(5):
    if R[i] % 10 != 0:
        p = min(p,R[i]%10)
ans = 0
for i in range(5):
    if R[i] % 10 != 0:
        if R[i] % 10 == p:
          ans += R[i]
          p = 10
        else:
          ans += R[i] - R[i] % 10 + 10
    else:
        ans += R[i]
print(ans)