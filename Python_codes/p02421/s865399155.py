game_time = int(input().strip())
game_cnt = 0
p_Taro = 0
p_Hanako = 0

while game_cnt < game_time:
    game_cnt = game_cnt + 1
    Taro, Hanako = input().split(" ")
    
    if Taro > Hanako:
        p_Taro = p_Taro + 3
    elif Taro < Hanako:
        p_Hanako = p_Hanako + 3
    else:
        p_Taro = p_Taro + 1
        p_Hanako = p_Hanako + 1
    
print(p_Taro, p_Hanako)