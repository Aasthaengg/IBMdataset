#B - Five Dishes 
import itertools
ABCDE = [int(input()) for _ in range(5)]
def calc(food):
    time = 0
    for i in food:
        if time % 10 != 0:
            while time % 10 != 0:
                time += 1    
        time += i
    return time
FOOD = list(itertools.permutations(ABCDE))

mini = 650
for j in FOOD:
        ans = calc(list(j))
        if mini > ans:
            mini = ans

print(mini)