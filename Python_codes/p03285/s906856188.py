N = int(input())
p = [i for i in range(101)]
q = [i for i in range(101)]
ans = 'No'

for a in p:
    for b in q:
        if 4*a+7*b == N:
            ans = 'Yes'
            break
        else:
            pass
print(ans)