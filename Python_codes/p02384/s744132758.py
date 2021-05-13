import random

class Dice():
    def __init__(self, numbers):
        self.numbers = numbers
        S = [1, 5, 2, 3, 0, 4]
        N = [4, 0, 2, 3, 5, 1]
        W = [3, 1, 0, 5, 4, 2]
        E = [2, 1, 5, 0, 4, 3]
        self.tumble = {0: S, 1: N, 2: W, 3: E}
        
    def rol(self, command):
        prev = self.numbers.copy()
        for i, t in enumerate(self.tumble[command]):
            self.numbers[t] = prev[i]
                
numbers = list(map(int, input().split()))
q = int(input())

dice = Dice(numbers)
for _ in range(q):
    query = list(map(int, input().split()))
    while True:
        dice.rol(random.randint(0, 3))
        if dice.numbers[0] == query[0] and dice.numbers[1] == query[1]:
            print(dice.numbers[2])
            break
