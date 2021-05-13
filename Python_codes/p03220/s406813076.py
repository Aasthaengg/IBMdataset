n = int(input())
t, a = map(int, input().split())
H = list(map(int, input().split()))
ABS = []
for i in H:
    ABS.append(abs((t-i*0.006) - a))
print(ABS.index(min(ABS)) + 1)