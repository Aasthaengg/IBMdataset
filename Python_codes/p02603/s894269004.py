class Assets:
    def __init__(self):
        self.money = 1000;self.stock = 0       
    
    def transaction(self, p_rate, n_rate = 0):

        if p_rate < n_rate and p_rate <= self.money:
            num = self.money // p_rate 
            self.stock += num
            self.money -= (num * p_rate)
        elif p_rate > n_rate :
            self.money += (p_rate * self.stock)
            self.stock = 0

    def show(self):
        print(self.money)

day = int(input())
rate_of_change = list(map(int, input().split()))

ans = Assets()

for j, i in enumerate(range(day) , 1):

    if j == day:
        Assets.transaction(ans, rate_of_change[i])
    else:        
        Assets.transaction(ans, rate_of_change[i], rate_of_change[j])

Assets.show(ans) 