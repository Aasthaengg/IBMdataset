N = int(input())

bot_a_cnt, top_b_cnt, bXa_cnt = 0, 0, 0
ab_cnt = 0

for i in range(N):
  S = input()
  top_b_cnt += 1 if S[0] == "B" else 0
  bot_a_cnt += 1 if S[-1] == "A" else 0
  bXa_cnt += 1 if S[0] == "B" and S[-1] == "A" else 0
  for j in range(len(S)-1):
    if S[j:j+2] == "AB":
      ab_cnt += 1
      
#print(bot_a_cnt, top_b_cnt, bXa_cnt, ab_cnt)
print(ab_cnt + min(bot_a_cnt, top_b_cnt) - (1 if bot_a_cnt > 0 and bot_a_cnt == top_b_cnt and top_b_cnt == bXa_cnt else 0))