N = int(input())
A_list = [int(e) for e in input().split()]

#bのうちどれか1つが偶数ならばOK
#bは3通り
#∴3**Nから全部が奇数のパターンを引けばOK

odd_pattern = 1

for i in range(N):
    if A_list[i]%2 == 0:
        odd_pattern *= 2
        
print(3**N - odd_pattern)