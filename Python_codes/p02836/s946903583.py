S=input()
pvt=int(len(S)/2)
f=S[:pvt]
b=S[pvt:]
b_sort=b[::-1]
ans=0
for i, j in zip(f,b_sort):
    if i != j:
        ans += 1
print(ans)
