import math

class Debt(object):
    def __init__(self):
        self.debt = 100000
        
    def spend_a_week(self):
        self.debt = self._ceil_1000(self.debt * 1.05)

    def _ceil_1000(self, debt):
        return int(math.ceil(debt / 1000) * 1000)

def run():
    n = int(input())
    debt = Debt()
    for _ in range(n):
        debt.spend_a_week()
    print(debt.debt)

if __name__ == '__main__':
    run()


