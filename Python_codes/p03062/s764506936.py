n = int(input())
la = [int(w) for w in input().split()]

ans = sum([abs(w)for w in la])
if len([w for w in la if w < 0]) % 2 == 0:
    print(ans)
    exit()

sla = sorted([abs(w)for w in la])
ans -= sla[0]*2
print(ans)
