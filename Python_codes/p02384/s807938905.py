class dice2():
    def __init__(self,men1,men2,men3,men4,men5,men6):
        self.men=[men1,men2,men3,men4,men5,men6]
        
    def find_num_rside(self,top,front):
        t=self.men.index(top)+1
        f=self.men.index(front)+1
        if [t,f] in [[1,2],[2,6],[6,5],[5,1]]:
            return self.men[3-1]#3
        elif  [t,f] in [[5,6],[6,2],[2,1],[1,5]]:
            return self.men[4-1]#4
        elif [t,f] in [[4,2],[2,3],[3,5],[5,4]]:
            return self.men[1-1]#1
        elif  [t,f] in [[5,3],[3,2],[2,4],[4,5]]:
            return self.men[6-1]#6
        elif  [t,f] in [[1,3],[3,6],[6,4],[4,1]]:
            return self.men[5-1]#5
        elif  [t,f] in [[4,6],[6,3],[3,1],[1,4]]:
            return self.men[2-1]#2
        
mn=list(map(int,input().split()))
q=int(input())

d=dice2(*mn)

for i in range(q):
    top, front=list(map(int,input().split()))
    ans=d.find_num_rside(top, front)
    print(ans)