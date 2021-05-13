class Heruistics:
    donelist = [0]*26
    resultlist = []
    contestlist = []

    def __init__(self,days):
        self.days = days
        self.clast = list(map(int,input().split()))
        self.allpref = [] #allpref[day][contest]
        for i in range(days):
            self.allpref.append(list(map(int,input().split())))

    def scoring(self,contlist):
        result = 0
        for i in range(self.days):
            cont = contlist[i]
            self.donelist[cont-1] = i+1
            zanen = sum([self.clast[j]*((i+1)-self.donelist[j]) for j in range(26)])

            result += self.allpref[i][cont-1] - zanen
            self.resultlist.append(result)

    def greedy(self):
        for i in range(self.days):
            max = -10**10
            result = 0
            contest = False
            for held in range(26):
                tempdonelist = self.donelist[:]
                tempdonelist[held] = i+1
                zanen = sum([self.clast[j]*((i+1)-tempdonelist[j]) for j in range(26)])
                result = self.allpref[i][held] - zanen
                if result >= max:
                    max = result;contest = held

            self.donelist[contest] = i+1
            self.contestlist.append(contest+1)


greed_heru = Heruistics(int(input()))
greed_heru.greedy()
#greed_heru.scoring(greed_heru.contestlist)
#for result in greed_heru.resultlist:
#    print(result)
for cont in greed_heru.contestlist:
    print(cont)
