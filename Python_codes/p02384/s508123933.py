class Dice2():
    def front(self,up,front,dice):
        #index == 5
        if(up==dice[2] and front==dice[1])or(up==dice[1] and front==dice[3])or(up==dice[3] and front==dice[4])or(up==dice[4] and front==dice[2]):
            return dice[5]
        #index == 4
        elif(up==dice[0] and front==dice[2])or(up==dice[2] and front==dice[5])or(up==dice[5] and front==dice[3])or(up==dice[3] and front==dice[0]):
            return dice[4]
        #index == 3
        elif(front==dice[5] and up==dice[4])or(front==dice[4] and up==dice[0])or(front==dice[0] and up==dice[1])or(front==dice[1] and up==dice[5]):
            return dice[3]
        #index == 2
        elif(up==dice[5] and front==dice[4])or(up==dice[4] and front==dice[0])or(up==dice[0] and front==dice[1])or(up==dice[1] and front==dice[5]):
            return dice[2]
        #index == 1
        elif(front==dice[0] and up==dice[2])or(front==dice[2] and up==dice[5])or(front==dice[5] and up==dice[3])or(front==dice[3] and up==dice[0]):
            return dice[1]
        #index == 0
        else:
            return dice[0]

dice = [int(i) for i in input().split()]
p = int(input())
dc2 = Dice2()
ans = []
for i in range(p):
    up,front = map(int,input().split())
    ans.append(dc2.front(up,front,dice))
for i in range(p):
    print(ans[i])
