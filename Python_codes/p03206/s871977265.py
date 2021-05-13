N = int(input())
check_eve=25

ans = ['Christmas']
for e in range(check_eve-N):
    ans.append('Eve')
    
print(' '.join(ans))