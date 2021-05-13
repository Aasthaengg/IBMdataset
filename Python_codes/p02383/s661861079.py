dice=input().split()
process=input()

do = {'N': (2,6,3,4,1,5),'S': (5,1,3,4,6,2),'E':(4,2,1,6,5,3),'W': (3,2,6,1,5,4)}

for x in process:
    dice=[dice[y-1] for y in do[x]]
print(dice[0])
