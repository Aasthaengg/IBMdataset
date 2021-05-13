othello = input()
bef = 0
sumall = 0
count = 0

for i in range(len(othello)):
    sumall += i
    if(othello[i] == 'B'):
        bef += i
        count += 1

sumelse = 0
for i in range(len(othello)-count):
    sumelse += i

aft = sumall - sumelse

print(aft - bef)