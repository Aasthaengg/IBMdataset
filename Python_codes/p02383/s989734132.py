class Dice:

    __top = 0
    __front = 1
    __right = 2
    __left = 3
    __back = 4
    __bottom = 5

    def __init__(self, a, b, c, d, e, f):
        self.__dice = [a,b,c,d,e,f]

    def S(self):
        dice_before = self.__dice[:]
        self.__dice[Dice.__top]    = dice_before[Dice.__back]
        self.__dice[Dice.__front]  = dice_before[Dice.__top]
        self.__dice[Dice.__right]  = dice_before[Dice.__right]
        self.__dice[Dice.__left]   = dice_before[Dice.__left]
        self.__dice[Dice.__back]   = dice_before[Dice.__bottom]
        self.__dice[Dice.__bottom] = dice_before[Dice.__front]

    def E(self):
        dice_before = self.__dice[:]
        self.__dice[Dice.__top]    = dice_before[Dice.__left]
        self.__dice[Dice.__front]  = dice_before[Dice.__front]
        self.__dice[Dice.__right]  = dice_before[Dice.__top]
        self.__dice[Dice.__left]   = dice_before[Dice.__bottom]
        self.__dice[Dice.__back]   = dice_before[Dice.__back]
        self.__dice[Dice.__bottom] = dice_before[Dice.__right]

    def W(self):
        dice_before = self.__dice[:]
        self.__dice[Dice.__top]    = dice_before[Dice.__right]
        self.__dice[Dice.__front]  = dice_before[Dice.__front]
        self.__dice[Dice.__right]  = dice_before[Dice.__bottom]
        self.__dice[Dice.__left]   = dice_before[Dice.__top]
        self.__dice[Dice.__back]   = dice_before[Dice.__back]
        self.__dice[Dice.__bottom] = dice_before[Dice.__left]

    def N(self):
        dice_before = self.__dice[:]
        self.__dice[Dice.__top]    = dice_before[Dice.__front]
        self.__dice[Dice.__front]  = dice_before[Dice.__bottom]
        self.__dice[Dice.__right]  = dice_before[Dice.__right]
        self.__dice[Dice.__left]   = dice_before[Dice.__left]
        self.__dice[Dice.__back]   = dice_before[Dice.__top]
        self.__dice[Dice.__bottom] = dice_before[Dice.__back]

    def top(self):
        return(self.__dice[Dice.__top])

a,b,c,d,e,f = input().split()
dice = Dice(a,b,c,d,e,f)
com = input()
for i in com:
    if i == 'S':
        dice.S()

    elif i == 'E':
        dice.E()

    elif i == 'W':
        dice.W()

    elif i == 'N':
        dice.N()

print(dice.top())