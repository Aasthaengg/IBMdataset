A, B, C, D = map(int, input().split())

cnt_T = -(-C//B)
cnt_A = -(-A//D)

ans = 'Yes' if cnt_T <= cnt_A else 'No'

print(ans)