n = list(input())

ans = 'No'

na = n[0:3]
nb = n[1::]

if all(i == na[0] for i in na) or all(j == nb[0] for j in nb):
    ans = 'Yes'

print(ans)