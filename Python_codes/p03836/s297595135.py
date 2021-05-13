sx, sy, tx, ty = map(int, input().split())

ans = ''

# 1回目の現在点から目的点への移動
cnt_ud = abs(ty-sy)
cnt_rl = abs(sx-tx)
ans += 'U'*cnt_ud+'R'*cnt_rl

# 1回目の目的点から現在点への移動
ans += 'D'*cnt_ud+'L'*cnt_rl

# 2回目の現在点から目的点への移動
ans += 'L'+'U'*(cnt_ud+1)+'R'*(cnt_rl+1)+'D'

# 2回目の目的点から現在点への移動
ans += 'R'+'D'*(cnt_ud+1)+'L'*(cnt_rl+1)+'U'

print(ans)
