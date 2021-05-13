def roll_N(self):
    self[0],self[1],self[4],self[5] = self[1],self[5],self[0],self[4]
def roll_W(self):
	self[0],self[2],self[3],self[5] = self[2],self[5],self[0],self[3]
dice = [int(e) for e in input().split()]
times = int(input())
for i in range(times):
    upper,front = map(int,input().split())
    rolleddice = list(dice)
    if front == rolleddice[2] or front == rolleddice[3]:
        roll_W(rolleddice)
    while front != rolleddice[1]:
        roll_N(rolleddice)
    while upper != rolleddice[0]:
        roll_W(rolleddice)
    print(rolleddice[2])
