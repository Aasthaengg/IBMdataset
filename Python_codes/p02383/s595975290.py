def roll(die, d):
    if d == "E":
        return [die[3], die[1], die[0], die[5], die[4], die[2]]
    if d == "N":
        return [die[1], die[5], die[2], die[3], die[0], die[4]]
    if d == "S":
        return [die[4], die[0], die[2], die[3], die[5], die[1]]
    if d == "W":
        return [die[2], die[1], die[5], die[0], die[4], die[3]]

die = list(map(int, input().split()))
queue = input()
for i in range(len(queue)):
    die = roll(die, queue[i])
print(die[0])