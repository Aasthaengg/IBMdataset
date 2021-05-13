max2 = lambda x,y: x if x > y else y
min2 = lambda x,y: x if x < y else y

N = int(input())

T = [0]*N
for i in range(N):
    T[int(input())-1] = i

m = 0
streak = 1
for a,b in zip(T,T[1:]):
    if a < b:
        streak += 1
    else:
        m = max2(m, streak)
        streak = 1
m = max2(m, streak)

print(N-m)
