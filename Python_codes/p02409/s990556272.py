nyukyo = [[[0 for i in range(10)] for m in range(3)] for n in range(4)]
num = int(input())
for i in range(num):
    handan = input().split()
    handan = list(map(int, handan))
    nyukyo[handan[0]-1][handan[1]-1][handan[2]-1] += handan[3]

for m in nyukyo[0]:
    t = list(map(str, m))
    print(" "+" ".join(t))
print("#"*20)
for m in nyukyo[1]:
    t = list(map(str, m))
    print(" "+" ".join(t))
print("#"*20)
for m in nyukyo[2]:
    t = list(map(str, m))
    print(" "+" ".join(t))
print("#"*20)
for m in nyukyo[3]:
    t = list(map(str, m))
    print(" "+" ".join(t))