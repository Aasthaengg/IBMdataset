class Heruistics:
    allpref = [] #allpref[day][contest]
    donelist = [0]*26
    resultlist = []
    contestlist = []

    def __init__(self,days):
        self.days = days
        self.clast = list(map(int,input().split()))
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

b_heru = Heruistics(int(input()))
for i in range(b_heru.days):
    b_heru.contestlist.append(int(input()))

b_heru.scoring(b_heru.contestlist)

for result in b_heru.resultlist:
    print(result)
