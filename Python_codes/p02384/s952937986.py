class Dice:
    def __init__(self, one: int, two: int, three: int, four: int, five: int, six: int) -> None:
        self.__one = one
        self.__two = two
        self.__three = three
        self.__four = four
        self.__five = five
        self.__six = six

    def roll(self, direction) -> None:
        if direction == "N":
            tmp = self.__one
            self.__one = self.__two
            self.__two = self.__six
            self.__six = self.__five
            self.__five = tmp

        if direction == "E":
            tmp = self.__one
            self.__one = self.__four
            self.__four = self.__six
            self.__six = self.__three
            self.__three = tmp

        if direction == "S":
            tmp = self.__one
            self.__one = self.__five
            self.__five = self.__six
            self.__six = self.__two
            self.__two = tmp

        if direction == "W":
            tmp = self.__one
            self.__one = self.__three
            self.__three = self.__six
            self.__six = self.__four
            self.__four = tmp

    def set_top(self, top: int) -> None:
        if dice.top != top:
            for i in range(3):
                dice.roll("N")
                if (dice.top == top):
                    break
        if dice.top != top:
            for i in range(3):
                dice.roll("E")
                if (dice.top == top):
                    break

    def rotate(self) -> None:
        tmp = self.__two
        self.__two = self.__four
        self.__four = self.__five
        self.__five = self.__three
        self.__three = tmp

    @property
    def top(self) -> int:
        return self.__one

    @property
    def front(self) -> int:
        return self.__two

    @property
    def right(self) -> int:
        return self.__three


if __name__ == "__main__":
    one, two, three, four, five, six = map(int, input().split(' '))
    dice = Dice(one, two, three, four, five, six)
    q = int(input())
    for i in range(q):
        top, front = map(int, input().split(' '))
        dice.set_top(top)
        while dice.front != front:
            dice.rotate()
        print(dice.right)

