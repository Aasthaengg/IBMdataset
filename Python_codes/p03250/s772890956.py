a, b, c = (input().split())
game = [a,b,c]
s_game = sorted(game , reverse =True)
# print(s_game)
ans1 = s_game[0]+ s_game[1]
# print(ans1)
ans = int(ans1) + int(s_game[2])
print(ans)