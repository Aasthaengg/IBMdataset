A,B,C,D = map(int, input())
ans = [str(A)]
for b in [B,-B]:
    for c in [C,-C]:
        for d in [D,-D]:
            if sum([A,b,c,d]) == 7:
                ans += ['+' + str(x) if x >= 0 else str(x) for x in [b,c,d]]
                print(''.join(ans) + '=7')
                exit(0)