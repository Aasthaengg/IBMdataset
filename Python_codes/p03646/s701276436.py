k = int(input())
base = k//50
ans = [i for i in range(base,base+51)]
for i in range(k%50):
    ans[i] += 50
    for j in range(50):
        if i!=j:
            ans[j] -= 1
print(50)
for i in range(50):
    print(ans[i],end=' ')
print()