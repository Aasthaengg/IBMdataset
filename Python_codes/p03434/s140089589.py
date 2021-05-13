
n = int(input())
a_list = list(map(int, input().split()))

a_list = sorted(a_list, reverse = True)

# print(a_list)

Alice_Score = 0
Bob_Score = 0

for i in range(n):

    # 奇数(1, 3, 5…)枚目はAliceのターン
    if i % 2 == 0 :
        Alice_Score = Alice_Score + a_list[i]
    else :
        Bob_Score = Bob_Score + a_list[i]

ans = Alice_Score - Bob_Score

print(ans)