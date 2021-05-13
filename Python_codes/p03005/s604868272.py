class BallDistribution:
    def __init__(self):
        self.N, self.K = map(int, input().split())

    def max_number(self):
        if self.K == 1:
            print(0)
        else:
            print(self.N - self.K)


ballDistribution = BallDistribution()
ballDistribution.max_number()
