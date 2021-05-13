class HowManyDivisors:
    def output(self, a, b, c):
        d = 0
        for i in range(a, b + 1, 1):
            if c % i == 0:
                d += 1
        print d

if __name__ == "__main__":
        hmd = HowManyDivisors()
        a, b, c = map(int, raw_input().split())
        hmd.output(a, b, c)