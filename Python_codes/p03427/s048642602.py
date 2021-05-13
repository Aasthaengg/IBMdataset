n = input()

ans = None
for i in n[1:]:
    if int(i) != 9:
        ans = int(n[0]) - 1 + sum([9]*(len(n)-1))
        break

if ans is None:
    ans = sum([ int(i) for i in list(n)  ])
       
print(ans)