S = list(input())
alf = 'abcdefghijklmnopqrstuvwxyz'
ans = 'None'
for i in range(len(alf)):
    if not alf[i] in S:
        ans = alf[i]
        break
print(ans)