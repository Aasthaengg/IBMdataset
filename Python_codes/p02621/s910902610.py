class tasi:

    def sum1(self,a):
        total = 0

        for i in range(3):
            total += a ** (i + 1)
    
        print(total)


a = int(input())
m = tasi()
m.sum1(a)

