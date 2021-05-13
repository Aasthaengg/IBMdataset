R,G,B,N = map(int, input().split())  

BALL = [0]*(N+100)
BALL[0] = 1

for num in range(0,N+1,1):
    if BALL[num] != 0 and num + R <= N:
        BALL[num+R] += BALL[num]
for num in range(0,N+1,1):
    if BALL[num] != 0 and num + G <= N:
        BALL[num+G] += BALL[num]

for num in range(0,N+1,1):
    if BALL[num] != 0 and num + B <= N:
        BALL[num+B] += BALL[num]

print(BALL[N])




