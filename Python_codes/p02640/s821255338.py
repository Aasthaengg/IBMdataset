n_all,leg_all=map(int, input().split())

for i in range(n_all+1):
    leg_kame=2*(n_all-i)
    leg_turu=4*i
    if leg_kame+leg_turu==leg_all:
        print('Yes')
        break
    else:
        continue
else:(print('No'))
