import math
result = []
while True:
    n = input()
    if n == 0:
        break;
    score = map(float,raw_input().split(" "))
    
    ave = sum(score)/len(score)

    alpha = math.sqrt(sum([(s-ave)**2 for s in score])/len(score))
    result.append(alpha)

for r in result:
    print r