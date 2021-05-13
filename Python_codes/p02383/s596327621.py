class Dice():
    def __init__(self, numbers):
        self.numbers = numbers
        S = [1, 5, 2, 3, 0, 4]
        N = [4, 0, 2, 3, 5, 1]
        W = [3, 1, 0, 5, 4, 2]
        E = [2, 1, 5, 0, 4, 3]
        self.tumble = {'S': S, 'N': N, 'W': W, 'E': E}
        
    def rol(self, command):
        prev = self.numbers.copy()
        for i, t in enumerate(self.tumble[command]):
            self.numbers[t] = prev[i]

numbers = list(map(int, input().split()))
commands = input()

dice = Dice(numbers)
for c in commands:
    dice.rol(c)
print(dice.numbers[0])
