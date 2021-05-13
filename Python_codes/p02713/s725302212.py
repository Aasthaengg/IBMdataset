import math
score = int(input())
answer = 0
gcd2 = 0
for i in range(score):
    for j in range(score):
        gcd2 = math.gcd(i+1,j+1)
        for k in range(score):
            answer += math.gcd(gcd2,k+1)
print(answer)